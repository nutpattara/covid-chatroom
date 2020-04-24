import json
from datetime import datetime

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from django.utils.timezone import localtime
from .models import Message, Room

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        room = Room.objects.get(room_name=self.room_name)
        messages = Message.objects.filter(room=room).order_by('-id')[:10][::-1]
        for message in messages:
            username = message.user.username
            text = message.message
            stamp = localtime(message.stamp).strftime("%d-%b-%Y (%H:%M:%S)")
            self.send(text_data=json.dumps({
                'username': username,
                'message': text,
                'stamp' : stamp
            }))
        

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        username = text_data_json['username']
        text = text_data_json['message']
        user = User.objects.get(username=username)
        room = Room.objects.get(room_name=self.room_name)

        message = Message.objects.create(
            user = user,
            message = text,
            room = room,
        )
        message.save()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username' : username,
                'message': text,
                'stamp' : message.stamp.strftime("%d-%b-%Y (%H:%M:%S)")
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        username = event['username']
        message = event['message']
        stamp = event['stamp']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'username': username,
            'message': message,
            'stamp' : stamp
        }))
