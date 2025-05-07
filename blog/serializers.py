from rest_framework import serializers
from .model import BlogsTable

class BlogsTableSerializer(serializers.Serializer):
    categoryId = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    created_date = serializers.CharField(max_length=255)
    image = serializers.CharField()
    def create(self, validated_data):
        return BlogsTable(**validated_data).save()
