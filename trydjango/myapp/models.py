from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.
import uuid
from django.contrib.auth import get_user_model
from datetime import datetime
User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    userId = models.IntegerField()
    userBio = models.TextField(blank=True)
    userProfileImg = models.ImageField(default="/blankpfp.jpg", null=True, blank=True)

    
    def __str__(self):
        return self.user.username



class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    caption=models.TextField(blank=True)
    userWhoPosted = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile1",null=True)
    postedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
