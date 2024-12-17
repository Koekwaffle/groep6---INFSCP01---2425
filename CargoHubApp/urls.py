from django.urls import path
from .views import (ClientView, InventoryView, ItemGroupView, ItemTypeView, ItemView, LocationView, 
                    OrderView, ShipmentView, SupplierView, TransferView, WarehouseView)
from .views import baseurl_view

urlpatterns = [
    path('', baseurl_view, name='baseurl'),
    path('clients/', ClientView.as_view(), name='client-list'),
    path('clients/<int:client_id>/', ClientView.as_view(), name='client-detail'),   
    path('inventories/', InventoryView.as_view(), name='inventories-list'),
    path('inventories/<int:client_id>/', InventoryView.as_view(), name='inventory-detail'),
    path('item_groups/', ItemGroupView.as_view(), name='item-groups-list'),
    path('item_groups/<int:client_id>/', ItemGroupView.as_view(), name='item_groups-detail'),
    path('item_types/', ItemTypeView.as_view(), name='item-types-list'),
    path('item_types/<int:client_id>/', ItemTypeView.as_view(), name='item_types-detail'),
    path('items/', ItemView.as_view(), name='items-list'),
    path('items/<str:client_id>/', ItemView.as_view(), name='items-detail'),
    path('locations/', LocationView.as_view(), name='locations-list'),
    path('locations/<int:client_id>/', LocationView.as_view(), name='location-detail'),
    path('orders/', OrderView.as_view(), name='orders-list'),
    path('orders/<int:client_id>/', OrderView.as_view(), name='orders-detail'),
    path('shipments/', ShipmentView.as_view(), name='shipments-list'),
    path('shipments/<int:client_id>/', ShipmentView.as_view(), name='shipment-detail'),
    path('suppliers/', SupplierView.as_view(), name='suppliers-list'),
    path('suppliers/<int:client_id>/', SupplierView.as_view(), name='supplier-detail'),
    path('transfers/', TransferView.as_view(), name='transfers-list'),
    path('transfers/<int:client_id>/', TransferView.as_view(), name='transfer-detail'),
    path('warehouses/', WarehouseView.as_view(), name='warehouses-list'),
    path('warehouses/<int:client_id>/', WarehouseView.as_view(), name='warehouse-detail'),
]
