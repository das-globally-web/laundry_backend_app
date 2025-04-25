from rest_framework import serializers
from .models import BannerTable

class BannerSerializer(serializers.Serializer):
    image = serializers.CharField(required=True, allow_blank=True)
    def create(self, validated_data):
        return BannerTable(**validated_data).save()
    


