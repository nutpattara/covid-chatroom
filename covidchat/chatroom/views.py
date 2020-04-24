from django.shortcuts import render, redirect
from django.http import HttpResponse
from chatroom_user.models import Profile
from .models import Room

def chat(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    data = {
        "rooms": profile.joined_room.all()
    }
    return render(request, 'chatroom/chat.html', data)

def createroom(request):
    data = {
        'create_error' : False
    }
    if request.method == 'POST':
        room_data = request.POST.dict()
        room_name = room_data['room_name']
        if Room.objects.filter(room_name=room_name).exists():
            data['create_error'] = True
            return render(request, 'chatroom/create.html', data)
        room = Room.objects.add(room_name)
        user = request.user
        profile = Profile.objects.get(user=user)
        profile.joined_room.add(room)
        data = {
            'room_name': room_name,
            'is_exists:': True
        }
        return redirect('chat')
    return render(request, 'chatroom/create.html', data)

def room(request, room_name):
    data = {
        'room_name': room_name,
        'is_exists:': False
    }
    room = Room.objects.filter(room_name=room_name)
    if room.exists():
        data['is_exists'] = True
        user = request.user
        profile = Profile.objects.get(user=user)
        if not room[0] in profile.joined_room.all():
            profile.joined_room.add(room[0])
            profile.save()
    return render(request, 'chatroom/room.html', data)

def leaveroom(request,room_name):
    data = {
        'room_name': room_name,
    }
    room = Room.objects.filter(room_name=room_name)
    user = request.user
    profile = Profile.objects.get(user=user)
    if room[0] in profile.joined_room.all():
        profile.joined_room.remove(room[0])
        profile.save()
    return redirect('chat')