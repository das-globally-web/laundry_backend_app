from rest_framework import serializers
from .models import SlotTable

class SlotSerializer(serializers.Serializer):
    startTime = serializers.CharField(max_length=30)
    endtime = serializers.CharField(max_length=30)
    pickup = serializers.BooleanField(default=False)
    def create(self, validated_data):
        return SlotTable(**validated_data).save()