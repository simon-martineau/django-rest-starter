from rest_framework import generics, viewsets

from apps.users.serializers import RegisterUserSerializer


class RegisterUserView(generics.CreateAPIView):
    """View to create a user"""
    serializer_class = RegisterUserSerializer
