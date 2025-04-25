# serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=20)
    country_code = serializers.CharField(max_length=10)
    current_address = serializers.CharField(max_length=500, required=False, allow_blank=True)

    profile_pic_url = serializers.CharField(required=False, allow_blank=True)
    staff = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return User(**validated_data).save()