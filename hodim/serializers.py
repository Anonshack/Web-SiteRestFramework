from rest_framework import serializers
from .models import hodim,Aboutpage,fikir,info,contact
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer

class HodimListSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']


class HodimSerializers(serializers.ModelSerializer):
    class Meta:
        model = hodim
        fields = ['id', 'name', 'lastname', 'bio', 'image']


class Aboutpageserializer(serializers.ModelSerializer):
    class Meta:
        model = Aboutpage
        fields = ['id','name','about','info','contact']


class fikirserializer(serializers.ModelSerializer):
    class Meta:
        model = fikir
        fields = ['title','link']


class infoserializer(serializers.ModelSerializer):
    class Meta:
        model = info
        fields = ['bio']


class contactserializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = ['tel','insta','tg','email']