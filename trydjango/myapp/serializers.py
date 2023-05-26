from rest_framework import serializers
from .models import Profile , Image
from django.contrib.auth.models import User



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class CurrUserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ('id' , 'username')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =Profile
        fields = '__all__'