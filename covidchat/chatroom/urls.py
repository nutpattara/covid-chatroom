from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('create', views.createroom, name='createroom'),
    path('leave/<str:room_name>/', views.leaveroom, name='leaveroom'),
    path('room/<str:room_name>/', views.room, name='room'),
]
