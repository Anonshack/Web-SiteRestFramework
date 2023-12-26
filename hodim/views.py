from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import hodim, Aboutpage, fikir, info, contact
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import (
    HodimSerializers,
    Aboutpageserializer,
    fikirserializer,
    infoserializer,
    contactserializer
)


class HodimAPIView(generics.ListAPIView):
    queryset = hodim.objects.all()
    serializer_class = HodimSerializers
    permission_classes = [IsAuthenticated]


class HodimCreateAPIView(generics.CreateAPIView):
    queryset = hodim.objects.all()
    serializer_class = HodimSerializers


class HodimUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = hodim.objects.all()
    serializer_class = HodimSerializers
    lookup_field = 'id'
    lookup_url_kwarg = 'hodim_id'


class AboutListAPIView(generics.ListAPIView):
    queryset = Aboutpage.objects.all()
    serializer_class = Aboutpageserializer
    permission_classes = [IsAuthenticated]


class fikirAPIView(generics.ListAPIView):
    queryset = fikir.objects.all()
    serializer_class = fikirserializer
    permission_classes = [IsAuthenticated]


class infoAPIView(generics.ListAPIView):
    queryset = info.objects.all()
    serializer_class = infoserializer
    permission_classes = [IsAuthenticated]


class ContactAPIView(generics.ListAPIView):
    queryset = fikir.objects.all()
    serializer_class = contactserializer
    permission_classes = [IsAuthenticated]
