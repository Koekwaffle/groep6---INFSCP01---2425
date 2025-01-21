from rest_framework import serializers
from .models import (Client, Inventory, ItemGroup, ItemLine, ItemType, Item, Location, Order, 
                     Shipment, Supplier, Transfer, Warehouse)

class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    zip_code = serializers.CharField(max_length=10)
    province = serializers.CharField(max_length=255)
    country = serializers.CharField(max_length=255)
    contact_name = serializers.CharField(max_length=255)
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


class ItemLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLine
        fields = '__all__'


class ItemSerializer(serializers.Serializer):
    uid = serializers.CharField(allow_null=True)
    code = serializers.CharField(allow_null=True)
    description = serializers.CharField(allow_null=True)
    short_description = serializers.CharField(allow_null=True)
    upc_code = serializers.CharField(allow_null=True)
    model_number = serializers.CharField(allow_null=True)
    commodity_code = serializers.CharField(allow_null=True)
    item_line = serializers.CharField(allow_null=True)  # Changed to CharField
    item_group = serializers.CharField(allow_null=True)  # Changed to CharField
    item_type = serializers.CharField(allow_null=True)  # Changed to CharField
    unit_purchase_quantity = serializers.CharField(allow_null=True)  # Changed to CharField
    unit_order_quantity = serializers.CharField(allow_null=True)  # Changed to CharField
    pack_order_quantity = serializers.CharField(allow_null=True)  # Changed to CharField
    supplier_id = serializers.CharField(allow_null=True)  # Changed to CharField
    supplier_code = serializers.CharField(allow_null=True)
    supplier_part_number = serializers.CharField(allow_null=True)
    created_at = serializers.CharField(allow_null=True)
    updated_at = serializers.CharField(allow_null=True)


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
