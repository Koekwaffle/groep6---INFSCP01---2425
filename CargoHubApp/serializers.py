from rest_framework import serializers
from .models import (Client, Inventory, ItemGroup, ItemLine, ItemType, Item, Location, Order, 
                     Shipment, Supplier, Transfer, Warehouse)

class ClientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=100)
    zip_code = serializers.CharField(max_length=20)
    province = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    contact_name = serializers.CharField(max_length=100)
    contact_phone = serializers.CharField(max_length=20)
    contact_email = serializers.EmailField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    
    class Meta:
        model = Client
        fields = '__all__'


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = '__all__'


class ItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemGroup
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'
