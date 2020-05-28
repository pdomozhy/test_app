from rest_framework import serializers
from django.contrib.auth import password_validation
from django.contrib.auth.models import BaseUserManager


from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = (
            'id',
            'app_id',
            'username',
            'email',
            'first_name',
            'last_name',
            'role',
            'is_confirmed',
            'shop',
        )


class RestrictedUserSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):

        read_only_fields = (
            'role',
            'is_confirmed',
            'shop',
        )


class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'})

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:

        model = User
        fields = (
            'username',
            'email',
            'password',
        )


class UserConfirmSerializer(serializers.ModelSerializer):

    token = serializers.UUIDField(source='app_id')

    class Meta:

        model = User
        fields = (
            'email',
            'token',
        )
