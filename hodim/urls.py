from django.urls import path
from .views import (
    HodimAPIView,
    HodimCreateAPIView,

    HodimUpdateAPIView,
    AboutListAPIView,

    fikirAPIView,
    infoAPIView,

    ContactAPIView
)
urlpatterns = [
    path('hodim/', HodimAPIView.as_view(), name='hodim'),
    path('hodim_create/', HodimCreateAPIView.as_view, name='hodim_qoshish'),

    path('hodim/<int:hodim_id>/', HodimUpdateAPIView.as_view(), name='hodim-detail'),
    path('about-page/', AboutListAPIView.as_view(), name='aboutpage'),

    path('fikir/', fikirAPIView.as_view(), name='fikir'),
    path('info/', infoAPIView.as_view(), name='info'),

    path('contact/', ContactAPIView.as_view(), name='contact')
]

