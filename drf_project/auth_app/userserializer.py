from rest_framework import serializers
from rest_framework.response import Response

from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def validate_email(self, value):
        data = UserModel.objects.filter(email=value)
        if data.exists():
            return serializers.ValidationError({"message": "User already exists"})
        return value
