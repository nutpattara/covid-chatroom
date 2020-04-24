from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from .models import Profile

def index(request):
    return render(request, 'chatroom_user/index.html')

def register(request):
    if request.method == 'POST':
        register_data = request.POST.dict()
        username = register_data.get('username')
        password = register_data.get('password')
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)
            profile.save()
            login_user = authenticate(username = username, password = password)
            login(request, login_user)
            return redirect('index')

        return HttpResponse('registration error')

    return render(request, 'registration/register.html')