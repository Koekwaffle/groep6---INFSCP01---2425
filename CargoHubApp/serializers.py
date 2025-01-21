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


class WarehouseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    code = serializers.CharField()
    name = serializers.CharField()
    address = serializers.CharField()
    city = serializers.CharField(required=False, allow_blank=True)
    province = serializers.CharField()
    country = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        if isinstance(instance, tuple):
            return {
                'id': instance[0],
                'code': instance[1],
                'name': instance[2],
                'address': instance[3],
                'city': instance[4] or '',
                'province': instance[5],
                'country': instance[6],
                'created_at': instance[7],
                'updated_at': instance[8]
            }
        return super().to_representation(instance)


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


class ShipmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    order_id = serializers.IntegerField()
    source_id = serializers.IntegerField()
    order_date = serializers.DateTimeField()
    request_date = serializers.DateTimeField()
    shipment_date = serializers.DateTimeField()
    shipment_type = serializers.CharField()
    shipment_status = serializers.CharField()
    notes = serializers.CharField(allow_blank=True)
    carrier_code = serializers.CharField()
    carrier_description = serializers.CharField()
    service_code = serializers.CharField()
    payment_type = serializers.CharField()
    transfer_mode = serializers.CharField()
    total_package_count = serializers.IntegerField()
    total_package_weight = serializers.FloatField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        if isinstance(instance, tuple):
            return {
                'id': instance[0],
                'order_id': instance[1],
                'source_id': instance[2],
                'order_date': instance[3],
                'request_date': instance[4],
                'shipment_date': instance[5],
                'shipment_type': instance[6],
                'shipment_status': instance[7],
                'notes': instance[8],
                'carrier_code': instance[9],
                'carrier_description': instance[10],
                'service_code': instance[11],
                'payment_type': instance[12],
                'transfer_mode': instance[13],
                'total_package_count': instance[14],
                'total_package_weight': instance[15],
                'created_at': instance[16],
                'updated_at': instance[17]
            }
        return super().to_representation(instance)


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'
