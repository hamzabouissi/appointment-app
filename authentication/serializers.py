from authentication.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializerOut(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    # email = serializers.EmailField()


class UserModelSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "email", "password")


class UserModelSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password")


class UserModelSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")

    def validate_password(self, value):
        value = make_password(value)
        return value

    def validate_first_name(self, value):
        if value[0] == "a":
            value = "alien"
        return value
