from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
        print("\n\n\n GETTING \n\n\n")
        print(request.query_params)
        if 'client_id' in request.query_params:
            print("\n\n\n GETTING CLIENT ID \n\n\n")
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
        shipment_id = kwargs.get('shipment_id')
        if shipment_id:
            shipment = self.model_instance().get(shipment_id)  # Use the correct method name
            if shipment:
                serializer = self.serializer_class(shipment)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"error": "Shipment not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            shipments = self.model_instance().get_all()  # Use the correct method name
            if not shipments:
                return JsonResponse({"message": "No shipments found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(shipments, many=True)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


class TransferView(GenericView):
    model = Transfers
    model_instance = Transfers
    serializer_class = TransferSerializer


class ItemLineView(GenericView):
    model = ItemLines
    model_instance = ItemLines
    serializer_class = ItemLineSerializer

from rest_framework import generics
from .permissions import APIKeyPermission

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
            inventory_model = self.model_instance()
            inventories = inventory_model.get_by_item(item_uid)
            if inventories:
                serializer = self.serializer_class(inventories, many=True)
                return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse({"message": "No inventory found for this item"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"Error in ItemInventoriesView: {str(e)}")
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ItemInventoryTotalsView(GenericView):
    model_instance = Inventories
    serializer_class = InventorySerializer
    
    def get(self, request, item_uid):
        try:
            inventory_model = self.model_instance()
            totals = inventory_model.get_inventory_totals(item_uid)
            if totals:
                return JsonResponse(totals, safe=False, status=status.HTTP_200_OK)
            return JsonResponse({"message": "No inventory totals found for this item"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"Error in ItemInventoryTotalsView: {str(e)}")
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

