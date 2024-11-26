from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (ClientSerializer, InventorySerializer, ItemGroupSerializer, ItemTypeSerializer, 
                          ItemSerializer, LocationSerializer, OrderSerializer, ShipmentSerializer, 
                          SupplierSerializer, TransferSerializer, WarehouseSerializer)
from rest_framework.exceptions import NotFound, ValidationError
from django.http import JsonResponse
from django.http import HttpResponse
from django.urls import path

from api.models.clients import Clients
from api.models.inventories import Inventories
from api.models.item_groups import Item_Groups
from api.models.item_lines import Item_Lines
from api.models.item_types import Item_Types
from api.models.items import Items
from api.models.locations import Locations
from api.models.orders import Orders
from api.models.shipments import Shipments
from api.models.suppliers import Suppliers
from api.models.transfers import Transfers
from api.models.warehouses import Warehouses

def baseurl_view(request):
    return HttpResponse("Welcome to the Cargohub API! :)", status=200)

class GenericView(APIView):
    model_class = None  # Will be set dynamically in child views
    model_instance = None  # Instance of the model used for DB operations
    serializer_class = None  # Used for serialization

    def get(self, request, *args, **kwargs):
        # Fetch the model's ID from kwargs if it exists
        model_instance = self.model_instance()  # Create an instance of the model

        if 'client_id' in kwargs:
            client_id = kwargs.get('client_id')
            client = model_instance.get(client_id)  # Call the specific model's method
            if client is None:
                return JsonResponse({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
            return JsonResponse(client, status=status.HTTP_200_OK)

        # For the general case (e.g., fetch all clients)
        clients = model_instance.gets()  # Fetch all clients
        if not clients:
            return JsonResponse({"message": "No clients found"}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse(clients, safe=False, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        model_instance = self.model_instance()  # Create an instance of the model
        client_data = request.data
        model_instance.add(client_data)  # Call the add method on the model instance
        return JsonResponse(client_data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        client_id = kwargs.get('client_id')
        if not client_id:
            return JsonResponse({"error": "client_id is required for update"}, status=status.HTTP_400_BAD_REQUEST)

        model_instance = self.model_instance()  # Create an instance of the model
        client_data = request.data
        model_instance.update(client_id, client_data)  # Update client data
        return JsonResponse(client_data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        client_id = kwargs.get('client_id')
        if not client_id:
            return JsonResponse({"error": "client_id is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)

        model_instance = self.model_instance()  # Create an instance of the model
        model_instance.remove(client_id)  # Call the remove method to delete
        return JsonResponse({"message": "Client deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    
class ClientView(GenericView):
    model_class = Clients  # Set the model class here
    model_instance = Clients  # Set the model instance class here
    serializer_class = ClientSerializer  # If you want to serialize data, use the serializer here


class WarehouseView(GenericView):
    model = Warehouses
    model_instance = Warehouses  # Set the model instance class here
    serializer_class = WarehouseSerializer  # If you want to serialize data, use the serializer here


class LocationView(GenericView):
    model = Locations
    model_instance = Locations
    serializer_class = LocationSerializer


class ItemTypeView(GenericView):
    model = Item_Types
    model_instance = Item_Types
    serializer_class = ItemTypeSerializer


class ItemGroupView(GenericView):
    model = Item_Groups
    model_instance = Item_Groups
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


class TransferView(GenericView):
    model = Transfers
    model_instance = Transfers
    serializer_class = TransferSerializer
