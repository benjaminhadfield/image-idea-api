from rest_framework import serializers

from apps.user_profile.serializers import UserProfileSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(source='userprofile')

    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'short_name',
            'date_joined',
            'profile',
        )
