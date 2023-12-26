from rest_framework import status,generics
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model, logout
from rest_framework.views import APIView
from .models import mijoz, aboutpage, Director, Asoschi
from .serializers import (
    MijozListSerializer,
    MijozSerializer,
    AboutpageSerializer,
    AsoschiSerializer,
    DirectorSerializer
)


class MijozAPIView(generics.ListAPIView):
    serializer_class = MijozListSerializer
    queryset = mijoz.objects.all()


class MijozUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = mijoz.objects.all()
    serializer_class = MijozSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'mijoz_id'


class MijozCreateAPIView(generics.CreateAPIView):
    queryset = mijoz.objects.all()
    serializer_class = MijozSerializer


class AboutListAPIView(generics.ListAPIView):
    queryset = aboutpage.objects.all()
    serializer_class = AboutpageSerializer


class DirectorAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]


class AsoschiAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]