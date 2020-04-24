from djongo import models
from django.contrib.auth.models import User
from chatroom.models import Room

class Profile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    joined_room = models.ManyToManyField(Room)

    def __str__(self):
        return f'{self.user.username} Profile'