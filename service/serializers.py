from rest_framework import serializers
from .models import ServiceTable

class ServiceSerializer(serializers.Serializer):
    banner_image = serializers.CharField(required=True, allow_blank=False)
    icon_image = serializers.CharField(required=True, allow_blank=True)
    title = serializers.CharField(max_length=500)
    rating = serializers.FloatField(required=True)
    def create(self, validated_data):
        return ServiceTable(**validated_data).save()