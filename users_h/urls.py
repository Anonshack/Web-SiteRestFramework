from django.urls import path
from .views import (
    UserRegisterView,
    UserLoginView,

    UsersListView,
    UserLogoutAPI,
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),

    path('users/', UsersListView.as_view(), name='users'),
    path('logout/', UserLogoutAPI.as_view(), name='logout'),
]
