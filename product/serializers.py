from rest_framework import serializers
from .models import ProductTable

class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    image = serializers.CharField(max_length=255)
    price_json =serializers.ListField(child=serializers.DictField())
    def create(self, validated_data):
        return ProductTable(**validated_data).save()