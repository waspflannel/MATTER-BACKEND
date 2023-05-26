from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Image
from django.forms import ModelForm

class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title','image','caption')
