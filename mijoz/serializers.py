from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer
from .models import mijoz,aboutpage,Director,Asoschi
User = get_user_model()


class MijozListSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']


class MijozSerializer(ModelSerializer):
    class Meta:
        model = mijoz     
        fields = ['id', 'name', 'lastname', 'bio', 'image']   


class AboutpageSerializer(ModelSerializer):
    class Meta:
        model = aboutpage
        fields = ['id', 'companiya', 'social', 'otzv', 'info']


class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = ['id','name', 'lastname', 'date', 'position', 'address','img']


class AsoschiSerializer(ModelSerializer):
    class Meta:
        model = Asoschi
        fields = ['id','name', 'lastname', 'date', 'position', 'address','img']