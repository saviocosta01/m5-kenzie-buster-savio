from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ]
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="email already registered."
            )
        ]
    )
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(required=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict):
        if validated_data.get("is_employee"):
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
