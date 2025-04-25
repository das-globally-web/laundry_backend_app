from rest_framework import serializers
from .models import OrderTable

class OrderSerializer(serializers.Serializer):
    order_id = serializers.CharField(max_length=255)
    userid = serializers.CharField(max_length=255)
    create_date = serializers.CharField(max_length=255)
    delivery_date = serializers.CharField(max_length=255)
    trx_id = serializers.CharField(max_length=255, required=False, allow_blank=True)
    payment_tpe = serializers.CharField(max_length=255)
    product = serializers.ListField(child=serializers.DictField())
    total_booked_amount = serializers.FloatField()
    iroing = serializers.BooleanField()
    barcode_path = serializers.CharField(max_length=255)
    qrcode_path =serializers.CharField(max_length=255)
    deliverd = serializers.BooleanField()
    address = serializers.CharField(max_length=255)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    user = serializers.DictField()
    delivery_slot = serializers.CharField(max_length=255)
    pickup_slot = serializers.CharField(max_length=255)
    def create(self, validated_data):
        # Remove MongoDB-specific _id fields if they exist
        for item in validated_data.get("product", []):
            if "product" in item and "_id" in item["product"]:
                item["product"].pop("_id")  # Remove MongoDB _id

        return OrderTable(**validated_data).save()