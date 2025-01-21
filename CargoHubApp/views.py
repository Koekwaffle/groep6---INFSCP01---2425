from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection  # Add this import
from .serializers import (ClientSerializer, InventorySerializer, ItemGroupSerializer, ItemTypeSerializer, 
                          ItemSerializer, LocationSerializer, OrderSerializer, ShipmentSerializer, 
                          SupplierSerializer, TransferSerializer, WarehouseSerializer, ItemLineSerializer)  # Import ItemLineSerializer
from rest_framework.exceptions import NotFound, ValidationError
from django.http import JsonResponse

from api.providers import auth_provider  # Import the auth_provider module
from audit_log import log_audit_event  # Correct the import path

# Initialize the auth_provider
auth_provider.init()

def get_user(api_key):
    return auth_provider.get_user(api_key)  # Use the auth_provider to get the user

from django.http import HttpResponse
from django.urls import path

from api.models.clients import Clients
from api.models.inventories import Inventories
from api.models.item_groups import ItemGroups
from api.models.item_lines import ItemLines
from api.models.item_types import ItemTypes
from api.models.items import Items
from api.models.locations import Locations
from api.models.orders import Orders
from api.models.shipments import Shipments
from api.models.suppliers import Suppliers
from api.models.transfers import Transfers
from api.models.warehouses import Warehouses
from api.providers.auth_provider import has_access

from rest_framework import generics
from .permissions import APIKeyPermission

def baseurl_view(request):
    return HttpResponse("Welcome to the Cargohub API! :)", status=200)

class GenericView(APIView):
    def check_api_key(self, request):
        print("Checking API Key...")
        print(f"Request Headers: {request.headers}")
        authorization_header = request.headers.get('Authorization')
        # print(f"\n\n\nAuthorization Header: {authorization_header}\n\n\n")
        if (authorization_header):
            if authorization_header.startswith("Bearer "):
                api_key = authorization_header.split(" ")[1]
            else:
                api_key = authorization_header
            print(f"API Key from headers: {api_key}")
            log_audit_event(api_key, f"{request.method} {request.path}")  # Log the API key usage
            user = get_user(api_key)
            if user is None:
                return None
            allowed = has_access(user, request.path, request.method)
            # print(f"\n\n\n\n\nAllowed: {allowed}\n\n\n\n\n\n\n")
            if not allowed:
                return None
            # print(f"User: {user}")
            return user
        return None

    def dispatch(self, request, *args, **kwargs):
        # print("\n\n\ndispatch called\n\n\n")
        user = self.check_api_key(request)
        if user is None:
            return JsonResponse({"error": "Invalid API Key"}, status=status.HTTP_403_FORBIDDEN)
        return super().dispatch(request, *args, **kwargs)
    model_class = None  # Will be set dynamically in child views
    model_instance = None  # Instance of the model used for DB operations
    serializer_class = None  # Used for serialization

    def get(self, request, *args, **kwargs):
        model_instance = self.model_instance()  # Create an instance of the model
        # print("\n\n\n GETTING \n\n\n")
        # print(request.query_params)
        if 'client_id' in request.query_params:
            # print("\n\n\n GETTING CLIENT ID \n\n\n")
            client_id = request.query_params.get('client_id')
            print(client_id)
            client = model_instance.get(client_id)  # Call the specific model's method
            if client is None:
                return JsonResponse({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
            return JsonResponse(client, safe=False, status=status.HTTP_200_OK)

        # For the general case (e.g., fetch all records)
        records = model_instance.get_all()  # Fetch all records
        if not records:
            return JsonResponse({"message": "No records found"}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse(records, safe=False, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        model_instance = self.model_instance()  # Create an instance of the model
        client_data = request.data
        model_instance.add(client_data)  # Call the add method on the model instance
        return JsonResponse(client_data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        obj_id = kwargs.get('client_id') or kwargs.get('item_line_id') or kwargs.get('id') or request.data.get('client_id') or request.data.get('item_line_id') or request.data.get('id')
        if not obj_id:
            return JsonResponse({"error": "ID is required for update"}, status=status.HTTP_400_BAD_REQUEST)

        model_instance = self.model_instance()  # Create an instance of the model
        obj_data = request.data
        model_instance.update(obj_id, obj_data)  # Update object data
        return JsonResponse(obj_data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        obj_id = kwargs.get('client_id') or kwargs.get('item_line_id') or kwargs.get('id') or request.data.get('client_id') or request.data.get('item_line_id') or request.data.get('id')
        if not obj_id:
            return JsonResponse({"error": "ID is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)

        model_instance = self.model_instance()  # Create an instance of the model
        model_instance.remove(obj_id)  # Call the remove method to delete
        return JsonResponse({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    
class ClientView(GenericView):
    model_class = Clients
    model_instance = Clients
    serializer_class = ClientSerializer

    def get(self, request, *args, **kwargs):
        print("\n\n\n GETTING CLIENT \n\n\n")
        client_id = kwargs.get('client_id')
        if client_id:
            # print("\n\n\n CLIENT ID GET \n\n\n")
            client = self.model_instance().get(client_id)  # Use the correct method name
            if client:
                # print("\n\n\n CLIENT FOUND \n\n\n")
                serializer = self.serializer_class(client)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # print("\n\n\n GETTING ALL CLIENTS \n\n\n")
            clients = self.model_instance().get_all()  # Use the correct method name
            if not clients:
                return JsonResponse({"message": "No clients found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(clients, many=True)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


class WarehouseView(GenericView):
    model_class = Warehouses
    model_instance = Warehouses  # Set the model instance class here
    serializer_class = WarehouseSerializer  # If you want to serialize data, use the serializer here

    def get(self, request, *args, **kwargs):
        warehouse_id = kwargs.get('warehouse_id')
        if warehouse_id:
            locations = self.model_instance().get_warehouse_locations(warehouse_id)
            if not locations:
                return JsonResponse({"error": "No locations found for this warehouse"}, status=status.HTTP_404_NOT_FOUND)
            serializer = LocationSerializer(locations, many=True)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        else:
            warehouses = self.model_instance().get_all()
            if not warehouses:
                return JsonResponse({"message": "No warehouses found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(warehouses, many=True)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        


class LocationView(GenericView):
    model = Locations
    model_instance = Locations
    serializer_class = LocationSerializer


class ItemTypeView(GenericView):
    model = ItemTypes
    model_instance = ItemTypes
    serializer_class = ItemTypeSerializer


class ItemGroupView(GenericView):
    model = ItemGroups
    model_instance = ItemGroups
    serializer_class = ItemGroupSerializer


class ItemView(GenericView):
    model = Items
    model_instance = Items
    serializer_class = ItemSerializer


class InventoryView(GenericView):
    model = Inventories
    model_instance = Inventories
    serializer_class = InventorySerializer


class OrderView(GenericView):
    model = Orders
    model_instance = Orders
    serializer_class = OrderSerializer


class SupplierView(GenericView):
    model = Suppliers
    model_instance = Suppliers
    serializer_class = SupplierSerializer


class ShipmentView(GenericView):
    model = Shipments
    model_instance = Shipments
    serializer_class = ShipmentSerializer

    def get(self, request, *args, **kwargs):
        model_instance = self.model_instance()
        shipment_id = kwargs.get('shipment_id')
        
        # Check if we're requesting items for a shipment
        if 'items' in request.path:
            if shipment_id:
                items = model_instance.get_items_in_shipment(shipment_id)
                if items:
                    return JsonResponse({"items": items}, status=status.HTTP_200_OK)
                return JsonResponse({"error": "No items found for this shipment"}, status=status.HTTP_404_NOT_FOUND)
            return JsonResponse({"error": "Shipment ID required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if we're requesting orders for a shipment
        if 'orders' in request.path:
            if shipment_id:
                orders = model_instance.get_orders_in_shipment(shipment_id)
                if orders:
                    return JsonResponse({"orders": orders}, status=status.HTTP_200_OK)
                return JsonResponse({"error": "No orders found for this shipment"}, status=status.HTTP_404_NOT_FOUND)
            return JsonResponse({"error": "Shipment ID required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Regular shipment get logic
        if shipment_id:
            shipment = model_instance.get(shipment_id)
            if shipment:
                serializer = self.serializer_class(shipment)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"error": "Shipment not found"}, status=status.HTTP_404_NOT_FOUND)
        
        shipments = model_instance.get_all()
        if not shipments:
            return JsonResponse({"message": "No shipments found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(shipments, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        model_instance = self.model_instance()
        shipment_id = kwargs.get('shipment_id')
        
        # Handle orders in shipment
        if 'orders' in request.path and shipment_id:
            orders = request.data.get('orders', [])
            if not isinstance(orders, list):
                return JsonResponse({"error": "Orders must be a list"}, status=status.HTTP_400_BAD_REQUEST)
                
            success = model_instance.update_orders_in_shipment(shipment_id, orders)
            if success:
                return JsonResponse({"message": "Orders updated successfully", "orders": orders}, status=status.HTTP_200_OK)
            return JsonResponse({"error": "Failed to update orders"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Handle items in shipment
        if 'items' in request.path and shipment_id:
            items = request.data.get('items', [])
            if not isinstance(items, list):
                return JsonResponse({"error": "Items must be a list"}, status=status.HTTP_400_BAD_REQUEST)
                
            success = model_instance.update_items_in_shipment(shipment_id, items)
            if success:
                return JsonResponse({"message": "Items updated successfully", "items": items}, status=status.HTTP_200_OK)
            return JsonResponse({"error": "Failed to update items"}, status=status.HTTP_400_BAD_REQUEST)
            
        # Regular shipment post logic
        return super().post(request, *args, **kwargs)


class ShipmentOrdersView(GenericView):
    model = Shipments
    model_instance = Shipments
    serializer_class = ShipmentSerializer

    def get(self, request, shipment_id=None):
        model_instance = self.model_instance()
        if shipment_id:
            orders = model_instance.get_orders_in_shipment(shipment_id)
            if orders:
                return JsonResponse({"orders": orders}, status=status.HTTP_200_OK)
            return JsonResponse({"error": "No orders found for this shipment"}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({"error": "Shipment ID required"}, status=status.HTTP_400_BAD_REQUEST)

class TransferView(GenericView):
    model = Transfers
    model_instance = Transfers
    serializer_class = TransferSerializer


class ItemLineView(GenericView):
    model = ItemLines
    model_instance = ItemLines
    serializer_class = ItemLineSerializer


class ItemGroupItemsView(GenericView):  # Change to inherit from GenericView
    model_instance = Items
    serializer_class = ItemSerializer
    
    def get(self, request, item_group_id):
        try:
            items_model = self.model_instance()
            items = items_model.get_by_group(item_group_id)
            if items:
                # Explicitly convert each item to a dictionary
                item_dicts = [dict(zip([
                    'uid', 'code', 'description', 'short_description', 
                    'upc_code', 'model_number', 'commodity_code', 
                    'item_line', 'item_group', 'item_type',
                    'unit_purchase_quantity', 'unit_order_quantity', 
                    'pack_order_quantity', 'supplier_id', 'supplier_code',
                    'supplier_part_number', 'created_at', 'updated_at'
                ], item)) for item in items]
                
                serializer = self.serializer_class(item_dicts, many=True)
                return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse({"message": "No items found for this group"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"Error in ItemGroupItemsView: {str(e)}")  # Add debug print
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ItemLineItemsView(GenericView):
    model_instance = Items
    serializer_class = ItemSerializer
    
    def get(self, request, item_line_id):
        try:
            items_model = self.model_instance()
            items = items_model.get_by_line(item_line_id)
            if items:
                serializer = self.serializer_class(items, many=True)
                return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse({"message": "No items found for this line"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"Error in ItemLineItemsView: {str(e)}")
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ItemTypeItemsView(GenericView):
    model_instance = Items
    serializer_class = ItemSerializer
    
    def get(self, request, item_type_id):
        try:
            items_model = self.model_instance()
            items = items_model.get_by_type(item_type_id)
            if items:
                serializer = self.serializer_class(items, many=True)
                return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse({"message": "No items found for this type"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"Error in ItemTypeItemsView: {str(e)}")
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ItemInventoriesView(GenericView):
    model_instance = Inventories
    serializer_class = InventorySerializer
    
    def get(self, request, item_uid):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        id,
                        item_id,
                        description,
                        item_reference,
                        location_id,
                        total_on_hand,
                        total_expected,
                        total_ordered,
                        total_allocated,
                        total_available,
                        created_at,
                        updated_at
                    FROM inventories 
                    WHERE item_id = %s
                """, [item_uid])
                rows = cursor.fetchall()
                
                if rows:
                    inventories = [dict(zip([
                        'id', 'item_id', 'description', 'item_reference',
                        'location_id', 'total_on_hand', 'total_expected',
                        'total_ordered', 'total_allocated', 'total_available',
                        'created_at', 'updated_at'
                    ], row)) for row in rows]
                    return JsonResponse(inventories, safe=False, status=200)
                return JsonResponse({"message": "No inventory found for this item"}, status=404)
        except Exception as e:
            print(f"Database error: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)

class ItemInventoryTotalsView(GenericView):
    model_instance = Inventories
    serializer_class = InventorySerializer
    
    def get(self, request, item_uid):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        COALESCE(SUM(total_on_hand), 0) as total_on_hand,
                        COALESCE(SUM(total_expected), 0) as total_expected,
                        COALESCE(SUM(total_ordered), 0) as total_ordered,
                        COALESCE(SUM(total_allocated), 0) as total_allocated,
                        COALESCE(SUM(total_available), 0) as total_available
                    FROM inventories 
                    WHERE item_id = %s
                """, [item_uid])
                row = cursor.fetchone()
                
                if row:
                    return JsonResponse({
                        'total_on_hand': row[0],
                        'total_expected': row[1],
                        'total_ordered': row[2],
                        'total_allocated': row[3],
                        'total_available': row[4]
                    }, status=200)
                return JsonResponse({"message": "No inventory found for this item"}, status=404)
        except Exception as e:
            print(f"Error in ItemInventoryTotalsView: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)
class TransferCommitView(GenericView):
    def post(self, request, transfer_id):
        transfer = Transfers().get(transfer_id)
        items = Transfers().get_items_in_transfer(transfer_id)
        from_location = transfer.get("transfer_from")
        to_location = transfer.get("transfer_to")
        for x in items:
            inventories = Inventories().get_inventories_for_item(x["item_id"])  # You can define this method in Inventories
            for y in inventories:
                if y["location_id"] == from_location:
                    y["total_on_hand"] -= x["amount"]
                elif y["location_id"] == to_location:
                    y["total_on_hand"] += x["amount"]
                # (Recalculate total_expected, total_available, etc.)
                Inventories().update_inventory(y["id"], y)  # You can define update_inventory() in Inventories
        transfer["transfer_status"] = "Processed"
        Transfers().update(transfer_id, transfer)
        return JsonResponse({"message": "Batch transfer committed."}, status=200)

class OrderItemsView(GenericView):
    def get(self, request, order_id):
        items = Orders().get_items_in_order(order_id)
        if not items:
            return JsonResponse({"message": "No items found for order"}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(items, safe=False, status=status.HTTP_200_OK)

    def post(self, request, order_id):
        updated_items = request.data.get("items", [])
        Orders().update_items_in_order(order_id, updated_items)
        return JsonResponse({"message": "Order items updated."}, status=200)

class SupplierItemsView(GenericView):
    def get(self, request, supplier_id):
        items = Suppliers().get_items_for_supplier(supplier_id)
        if not items:
            return JsonResponse({"message": "No items found for this supplier"}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(items, safe=False, status=status.HTTP_200_OK)

