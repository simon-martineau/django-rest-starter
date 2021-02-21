from rest_framework import generics

from apps.users.serializers import RegisterUserSerializer


class CreateUserView(generics.CreateAPIView):
    """View to create a user"""
    serializer_class = RegisterUserSerializer
