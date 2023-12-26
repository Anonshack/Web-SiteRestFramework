from django.urls import path
from .views import (
    MijozAPIView,
    MijozCreateAPIView,

    MijozUpdateAPIView,
    AboutListAPIView,

    AsoschiAPIView,
    DirectorAPIView
)
urlpatterns = [
    path('mijoz/', MijozAPIView.as_view(), name='mijoz'),
    path('mijoz_create/', MijozCreateAPIView.as_view, name='mijoz_qoshish'),

    path('mijoz/<int:mijoz_id>/', MijozUpdateAPIView.as_view(), name='mijoz-detail'),
    path('about/', AboutListAPIView.as_view(), name='aboutpage'),

    path('asoschi/', AsoschiAPIView.as_view(), name='asoschi'),
    path('director/', DirectorAPIView.as_view(), name='asoschi')
]
