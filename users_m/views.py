from datetime import datetime, timedelta
import jwt
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model, logout
from rest_framework.views import APIView
from .serializers import (
    RegistrationSerializer,
    UsersListSerializer,
)
User = get_user_model()


class UserRegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserLoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username, is_active=True).first()

        if user is None:
            raise AuthenticationFailed('Login yoki parol xato, iltimos tekshirib qaytadan kiriting')

        if not user.check_password(password):
            raise AuthenticationFailed('Login yoki parol xato, iltimos tekshirib qaytadan kiriting')

        payload = {
            'username': user.username,
            'exp': datetime.utcnow() + timedelta(minutes=100),
            'iat': datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.data = {
            'token': token
        }
        return response


def checkUserToken(token):
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except:
        return False
    user = User.objects.filter(username=payload['username']).first()
    if user:
        return user

    return False


class UsersListView(ListAPIView):
    serializer_class = UsersListSerializer
    queryset = User.objects.all()


class UserLogoutAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response({"Message": "You are logged out successfully"}, status=status.HTTP_200_OK)
