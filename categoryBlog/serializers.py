from rest_framework import serializers
from .model import BlogCategory

class BlogCategorySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    def create(self, validated_data):
        return BlogCategory(**validated_data).save()