from django.utils import timezone

from djongo import models
from django.contrib.auth.models import User

class RoomManager(models.Manager):
    def add(self, room_name):
        room, created = Room.objects.get_or_create(room_name=room_name)
        return room

    def remove(self, room_name):
        try:
            room = Room.objects.get(room_name=room_name)
            room.delete()
        except Room.DoesNotExist:
            return

class Room(models.Model):
    room_name = models.CharField(
        max_length=255, unique=True, help_text="Group channel name for this room"
    )

    objects = RoomManager()

class Message(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)
    message = models.TextField(max_length=500, blank=True)
    stamp = models.DateTimeField(default=timezone.localtime)