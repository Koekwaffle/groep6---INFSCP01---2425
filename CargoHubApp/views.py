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

def baseurl_view(request):
    return HttpResponse("Welcome to the Cargohub API! :)", status=200)

class GenericView(APIView):
    model_class = None  # Will be set dynamically in child views
    model_instance = None  # Instance of the model used for DB operations
    serializer_class = None  # Used for serialization

    def get(self, request, *args, **kwargs):
        # Fetch the model's ID from kwargs if it exists
        model_instance = self.model_instance()  # Create an instance of the model

        if 'client_id' in request.query_params:
            client_id = request.query_params.get('client_id')
            print(client_id)
            client = model_instance.get(client_id)  # Call the specific model's method
            if client is None:
                return JsonResponse({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
            return JsonResponse(client, safe=False, status=status.HTTP_200_OK)

        # if 'commit_id' in request.query_params:
        #     commit_id = request.query_params.get('commit_id')
        #     commit = model_instance.get(commit_id)
        #     for x in commit['items']:
        #         inventories = model_instance.get_inventories_for_item(x['item_id'])
        #         for y in inventories:
        #             if y["location_id"] == client["transfer_from"]:
        #                 y["total_on_hand"] -= x["amount"]
        #                 y["total_expected"] = y["total_on_hand"] + y["total_ordered"]
        #                 y["total_available"] = y["total_on_hand"] - y["total_allocated"]
        #                 model_instance.update_inventory(y["id"], y)
        #             elif y["location_id"] == client["transfer_to"]:
        #                 y["total_on_hand"] += x["amount"]
        #                 y["total_expected"] = y["total_on_hand"] + y["total_ordered"]
        #                 y["total_available"] = y["total_on_hand"] - y["total_allocated"]
        #                 model_instance.update_inventory(y["id"], y)

        # For the general case (e.g., fetch all clients)
        clients = model_instance.get_all()  # Fetch all clients
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


class TransferView(GenericView):
    model = Transfers
    model_instance = Transfers
    serializer_class = TransferSerializer
