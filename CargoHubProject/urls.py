"""
URL configuration for CargoHubProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from CargoHubApp.views import (
    ClientView, WarehouseView, LocationView, ItemTypeView, ItemGroupView, 
    ItemView, InventoryView, OrderView, SupplierView, ShipmentView, 
    TransferView, ItemLineView
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="My Project API",
        default_version='v1',
        description="API documentation for My Project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('CargoHubApp.urls')),  # Make sure this line exists
    path('api/v1/', include([
        path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('clients/', ClientView.as_view(), name='client-list'),
        path('clients/<int:client_id>/', ClientView.as_view(), name='client-detail'),
        path('clients/<int:client_id>/orders/', OrderView.as_view(), name='client-orders'),
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
        path('warehouses/<int:client_id>/', WarehouseView.as_view(), name='warehouse-detail'),
        path('warehouses/', WarehouseView.as_view(), name='warehouses-list'),
        path('item_lines/', ItemLineView.as_view(), name='item-lines-list'),  # Add this line
        path('item_lines/<int:item_line_id>/', ItemLineView.as_view(), name='item-line-detail'),  # Add this line
    ])),
]
