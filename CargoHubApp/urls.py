from django.urls import path
from .views import (ClientView, InventoryView, ItemGroupView, ItemTypeView, ItemView, LocationView, 
                    OrderView, ShipmentView, SupplierView, TransferView, WarehouseView, ShipmentOrdersView)
                    OrderView, ShipmentView, SupplierView, TransferView, WarehouseView, ItemGroupItemsView, 
                    ItemLineItemsView, ItemTypeItemsView, ItemInventoriesView, ItemInventoryTotalsView)  # Add ItemLineItemsView, ItemTypeItemsView, and ItemInventoryTotalsView
from .views import baseurl_view

from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="CargoHub API",
        default_version='v1',
        description="API documentation for CargoHub",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(),
)


urlpatterns = [
    path('', baseurl_view, name='baseurl'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('clients/', ClientView.as_view(), name='clients'),
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
    path('suppliers/', SupplierView.as_view(), name='suppliers-list'),
    path('suppliers/<int:client_id>/', SupplierView.as_view(), name='supplier-detail'),
    path('transfers/', TransferView.as_view(), name='transfers-list'),
    path('transfers/<int:client_id>/', TransferView.as_view(), name='transfer-detail'),
    path('warehouses/', WarehouseView.as_view(), name='warehouses'),
    path('warehouses/<int:client_id>/', WarehouseView.as_view(), name='warehouse-detail'),
    path('shipments/<int:shipment_id>/orders/', ShipmentOrdersView.as_view(), name='shipment-orders'),
    path('shipments/<int:shipment_id>/items/', ShipmentView.as_view(), name='shipment-items'),
    path('shipments/<int:client_id>/', ShipmentView.as_view(), name='shipment-detail'),
    path('item_groups/<int:item_group_id>/items/', ItemGroupItemsView.as_view(), name='item-group-items'),  # Fixed path
    path('item_lines/<int:item_line_id>/items/', ItemLineItemsView.as_view(), name='item-line-items'),  # Add new path
    path('item_types/<int:item_type_id>/items/', ItemTypeItemsView.as_view(), name='item-type-items'),  # Add new path
    path('items/<str:item_uid>/inventories/', ItemInventoriesView.as_view(), name='item-inventories'),  # Add new path
    path('items/<str:item_uid>/inventory/totals/', ItemInventoryTotalsView.as_view(), name='item-inventory-totals'),  # Add new path
    path('warehouses/<int:warehouse_id>/locations/', WarehouseView.as_view(), name='warehouse-locations'),  # Fixed path
    path('transfers/<int:transfer_id>/commit/', TransferCommitView.as_view(), name='transfer-commit'),
    path('orders/<int:order_id>/items/', OrderItemsView.as_view(), name='order-items'),
    path('suppliers/<int:supplier_id>/items/', SupplierItemsView.as_view(), name='supplier-items'),
]
