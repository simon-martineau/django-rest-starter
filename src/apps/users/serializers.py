from django.http import HttpRequest
from rest_framework import serializers

from apps.users.models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5},
        }

    def create(self, validated_data: dict):
        """Create a new user with encrypted password and return it"""
        return User.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for the Profile object"""
    is_self = serializers.SerializerMethodField()

    def get_is_self(self, obj: Profile) -> bool:
        """Returns if the user being serialized is the authenticated user"""
        request: HttpRequest = self.context.get('request')
        if request:
            if request.user.is_authenticated:
                return obj == request.user.profile
        return False

    class Meta:
        model = Profile
        fields = ('username', 'is_self')
