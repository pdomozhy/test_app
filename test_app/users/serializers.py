from rest_framework import serializers


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
