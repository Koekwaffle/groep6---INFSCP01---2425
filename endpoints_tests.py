import requests
import pytest

BASE_URL = 'http://127.0.0.1:8000'
API_KEY = "a1b2c3d4e5"

########################## 
### Client endpoint tests 
########################## 
def test_1_post_new_client():
    data = {
        "name": "Test Client",
        "address": "Test Street 123",
        "city": "Test City",
        "zip_code": "1234AB",
        "province": "Test Province",
        "country": "Test Country",
        "contact_name": "Test Contact",
        "contact_phone": "06-12345678",
        "contact_email": "test.client@example.com"
    }
    response = requests.post(f"{BASE_URL}/api/v1/clients/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201

def test_2_get_new_client():
    response = requests.get(f"{BASE_URL}/api/v1/clients/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Client"
    assert data["address"] == "Test Street 123"
    assert data["city"] == "Test City"
    assert data["zip_code"] == "1234AB"
    assert data["province"] == "Test Province"
    assert data["country"] == "Test Country"
    assert data["contact_name"] == "Test Contact"
    assert data["contact_phone"] == "06-12345678"
    assert data["contact_email"] == "test.client@example.com"

def test_3_put_update_client():
    data = {
        "id": 99999,
        "name": "Updated Test Client",
        "address": "Updated Street 123",
        "city": "Updated City",
        "zip_code": "5678CD",
        "province": "Updated Province",
        "country": "Updated Country",
        "contact_name": "Updated Contact",
        "contact_phone": "06-87654321",
        "contact_email": "updated.test.client@example.com"
    }
    response = requests.put(f"{BASE_URL}/api/v1/clients/99999/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200

def test_4_get_updated_client():
    response = requests.get(f"{BASE_URL}/api/v1/clients/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Test Client"
    assert data["address"] == "Updated Street 123"
    assert data["city"] == "Updated City"
    assert data["zip_code"] == "5678CD"
    assert data["province"] == "Updated Province"
    assert data["country"] == "Updated Country"
    assert data["contact_name"] == "Updated Contact"
    assert data["contact_phone"] == "06-87654321"
    assert data["contact_email"] == "updated.test.client@example.com"

def test_5_delete_client():
    response = requests.delete(f"{BASE_URL}/api/v1/clients/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 204

def test_6_get_deleted_client():
    response = requests.get(f"{BASE_URL}/api/v1/clients/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 404

def test_7_get_all_clients():
    response = requests.get(f"{BASE_URL}/api/v1/clients/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200

############################## 
### Inventory endpoint tests 
##############################
def test_1_post_new_inventory():
    data = {
        "item_id": "P990002",
        "description": "Test Inventory",
        "item_reference": "TEST-REF",
        "locations": [12345, 67890],
        "total_on_hand": 100,
        "total_expected": 50,
        "total_ordered": 20,
        "total_allocated": 10,
        "total_available": 90
    }
    response = requests.post(f"{BASE_URL}/api/v1/inventories/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201

def test_2_get_new_inventory():
    response = requests.get(f"{BASE_URL}/api/v1/inventories/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == "P990002"
    assert data["description"] == "Test Inventory"
    assert data["item_reference"] == "TEST-REF"
    assert data["locations"] == [12345, 67890]
    assert data["total_on_hand"] == 100
    assert data["total_expected"] == 50
    assert data["total_ordered"] == 20
    assert data["total_allocated"] == 10
    assert data["total_available"] == 90

def test_3_put_update_inventory():
    data = {
        "id": 99999,
        "item_id": "P990002",
        "description": "Updated Test Inventory",
        "item_reference": "UPDATED-TEST-REF",
        "locations": [12345, 67890],
        "total_on_hand": 150,
        "total_expected": 60,
        "total_ordered": 30,
        "total_allocated": 20,
        "total_available": 110
    }
    response = requests.put(f"{BASE_URL}/api/v1/inventories/99999/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200

def test_4_get_updated_inventory():
    response = requests.get(f"{BASE_URL}/api/v1/inventories/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == "P990002"
    assert data["description"] == "Updated Test Inventory"
    assert data["item_reference"] == "UPDATED-TEST-REF"
    assert data["locations"] == [12345, 67890]
    assert data["total_on_hand"] == 150
    assert data["total_expected"] == 60
    assert data["total_ordered"] == 30
    assert data["total_allocated"] == 20
    assert data["total_available"] == 110

def test_5_delete_inventory():
    response = requests.delete(f"{BASE_URL}/api/v1/inventories/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 204

def test_6_get_deleted_inventory():
    response = requests.get(f"{BASE_URL}/api/v1/inventories/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 404

def test_7_get_all_inventories():
    response = requests.get(f"{BASE_URL}/api/v1/inventories/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200

############################### 
### Item Groups endpoint tests 
############################### 
def test_1_post_new_item_group():
    data = {
        "uid": "P000084",
        "code": "xQk78654R",
        "description": "Open-architected tertiary contingency",
        "short_description": "throughout",
        "upc_code": "6240362357099",
        "model_number": "81-buCQA7M",
        "commodity_code": "hV-9935",
        "item_line": 67,
        "item_group": 1,
        "item_type": 17,
        "unit_purchase_quantity": 18,
        "unit_order_quantity": 17,
        "pack_order_quantity": 13,
        "supplier_id": 27,
        "supplier_code": "SUP545",
        "supplier_part_number": "f-768-s2A",
        "created_at": "1995-09-07 07:15:07",
        "updated_at": "1996-09-16 17:31:21"
    }
    response = requests.post(f"{BASE_URL}/api/v1/item_groups/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201

def test_2_get_new_item_group():
    response = requests.get(f"{BASE_URL}/api/v1/item_groups/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["uid"] == "P000084"
    assert data["code"] == "xQk78654R"
    assert data["description"] == "Open-architected tertiary contingency"
    assert data["short_description"] == "throughout"
    assert data["upc_code"] == "6240362357099"
    assert data["model_number"] == "81-buCQA7M"
    assert data["commodity_code"] == "hV-9935"
    assert data["item_line"] == 67
    assert data["item_group"] == 1
    assert data["item_type"] == 17

def test_3_put_update_item_group():
    data = {
        "id": 99999,
        "name": "Updated Electronics",
        "description": "Updated description for the electronics group",
        "created_at": "1998-05-15 19:52:53",
        "updated_at": "2024-09-30 12:50:00"
    }
    response = requests.put(f"{BASE_URL}/api/v1/item_groups/99999/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200

def test_4_get_updated_item_group():
    response = requests.get(f"{BASE_URL}/api/v1/item_groups/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Electronics"
    assert data["description"] == "Updated description for the electronics group"

def test_5_delete_item_group():
    response = requests.delete(f"{BASE_URL}/api/v1/item_groups/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 204

def test_6_get_deleted_item_group():
    response = requests.get(f"{BASE_URL}/api/v1/item_groups/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 404

def test_7_get_all_item_groups():
    response = requests.get(f"{BASE_URL}/api/v1/item_groups/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200

############################### 
### Item Lines endpoint tests 
############################### 
def test_1_post_new_item_line():
    data = {
        "name": "New Item Line",
        "description": "This is a new item line"
    }
    response = requests.post(f"{BASE_URL}/api/v1/item_lines/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201

def test_2_get_new_item_line():
    response = requests.get(f"{BASE_URL}/api/v1/item_lines/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "New Item Line"
    assert data["description"] == "This is a new item line"

def test_3_put_update_item_line():
    data = {
        "id": 99999,
        "name": "Updated Item Line Name",
        "description": "Updated description for item line",
        "created_at": "2010-01-01 12:00:00",
        "updated_at": "2024-09-30 13:00:00"
    }
    response = requests.put(f"{BASE_URL}/api/v1/item_lines/99999/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200

def test_4_get_updated_item_line():
    response = requests.get(f"{BASE_URL}/api/v1/item_lines/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Item Line Name"
    assert data["description"] == "Updated description for item line"

def test_5_delete_item_line():
    response = requests.delete(f"{BASE_URL}/api/v1/item_lines/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 204

def test_6_get_deleted_item_line():
    response = requests.get(f"{BASE_URL}/api/v1/item_lines/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 404

def test_7_get_all_item_lines():
    response = requests.get(f"{BASE_URL}/api/v1/item_lines/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200

############################### 
### Locations endpoint tests 
############################### 
def test_1_post_new_location():
    data = {
        "warehouse_id": 1,
        "code": "A.1.1",
        "name": "Row: A, Rack: 1, Shelf: 1"
    }
    response = requests.post(f"{BASE_URL}/api/v1/locations/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201

def test_2_get_new_location():
    response = requests.get(f"{BASE_URL}/api/v1/locations/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["warehouse_id"] == 1
    assert data["code"] == "A.1.1"
    assert data["name"] == "Row: A, Rack: 1, Shelf: 1"

def test_3_put_update_location():
    data = {
        "name": "Updated Location Name",
        "address": "123 Updated Street",
        "city": "Updated City",
        "province": "Updated Province",
        "country": "Updated Country"
    }
    response = requests.put(f"{BASE_URL}/api/v1/locations/99999/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200

def test_4_get_updated_location():
    response = requests.get(f"{BASE_URL}/api/v1/locations/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Location Name"
    assert data["address"] == "123 Updated Street"
    assert data["city"] == "Updated City"
    assert data["province"] == "Updated Province"
    assert data["country"] == "Updated Country"

def test_5_delete_location():
    response = requests.delete(f"{BASE_URL}/api/v1/locations/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 204

def test_6_get_deleted_location():
    response = requests.get(f"{BASE_URL}/api/v1/locations/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 404

def test_7_get_all_locations():
    response = requests.get(f"{BASE_URL}/api/v1/locations/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200

############################### 
### Orders endpoint tests 
############################### 
def test_1_post_new_order():
    data = {
        "client_id": 1,
        "reference": "ORDER123",
        "date_required": "2024-02-01",
        "status": "new"
    }
    response = requests.post(f"{BASE_URL}/api/v1/orders/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201

def test_2_get_new_order():
    response = requests.get(f"{BASE_URL}/api/v1/orders/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["client_id"] == 1
    assert data["reference"] == "ORDER123"
    assert data["date_required"] == "2024-02-01"
    assert data["status"] == "new"

def test_3_put_update_order():
    data = {
        "client_id": 1,
        "reference": "UPDATED-ORDER123",
        "date_required": "2024-02-02",
        "status": "processing"
    }
    response = requests.put(f"{BASE_URL}/api/v1/orders/99999/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200

def test_4_get_updated_order():
    response = requests.get(f"{BASE_URL}/api/v1/orders/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["client_id"] == 1
    assert data["reference"] == "UPDATED-ORDER123"
    assert data["date_required"] == "2024-02-02"
    assert data["status"] == "processing"

def test_5_delete_order():
    response = requests.delete(f"{BASE_URL}/api/v1/orders/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 204

def test_6_get_deleted_order():
    response = requests.get(f"{BASE_URL}/api/v1/orders/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 404

def test_7_get_all_orders():
    response = requests.get(f"{BASE_URL}/api/v1/orders/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200

############################### 
### Items endpoint tests 
############################### 
def test_1_post_new_item():
    data = {
        "uid": "P000001",
        "code": "ITEM123",
        "description": "New test item",
        "item_group": 1,
        "item_line": 1
    }
    response = requests.post(f"{BASE_URL}/api/v1/items/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201

def test_2_get_new_item():
    response = requests.get(f"{BASE_URL}/api/v1/items/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["uid"] == "P000001"
    assert data["code"] == "ITEM123"
    assert data["description"] == "New test item"
    assert data["item_group"] == 1
    assert data["item_line"] == 1

def test_3_put_update_item():
    data = {
        "uid": "P000001",
        "code": "UPDATED-ITEM123",
        "description": "Updated test item",
        "item_group": 1,
        "item_line": 1
    }
    response = requests.put(f"{BASE_URL}/api/v1/items/99999/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200

def test_4_get_updated_item():
    response = requests.get(f"{BASE_URL}/api/v1/items/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["uid"] == "P000001"
    assert data["code"] == "UPDATED-ITEM123"
    assert data["description"] == "Updated test item"
    assert data["item_group"] == 1
    assert data["item_line"] == 1

def test_5_delete_item():
    response = requests.delete(f"{BASE_URL}/api/v1/items/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 204

def test_6_get_deleted_item():
    response = requests.get(f"{BASE_URL}/api/v1/items/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 404

def test_7_get_all_items():
    response = requests.get(f"{BASE_URL}/api/v1/items/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200

############################### 
### Warehouses endpoint tests 
############################### 
def test_1_post_new_warehouse():
    data = {
        "name": "New Warehouse",
        "address": "123 Warehouse St",
        "city": "Warehouse City",
        "province": "WH",
        "country": "Netherlands"
    }
    response = requests.post(f"{BASE_URL}/api/v1/warehouses/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201

def test_2_get_new_warehouse():
    response = requests.get(f"{BASE_URL}/api/v1/warehouses/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "New Warehouse"
    assert data["address"] == "123 Warehouse St"
    assert data["city"] == "Warehouse City"
    assert data["province"] == "WH"
    assert data["country"] == "Netherlands"

def test_3_put_update_warehouse():
    data = {
        "name": "Updated Warehouse",
        "address": "456 Updated St",
        "city": "Updated City",
        "province": "UP",
        "country": "Netherlands"
    }
    response = requests.put(f"{BASE_URL}/api/v1/warehouses/99999/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200

def test_4_get_updated_warehouse():
    response = requests.get(f"{BASE_URL}/api/v1/warehouses/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Warehouse"
    assert data["address"] == "456 Updated St"
    assert data["city"] == "Updated City"
    assert data["province"] == "UP"
    assert data["country"] == "Netherlands"

def test_5_delete_warehouse():
    response = requests.delete(f"{BASE_URL}/api/v1/warehouses/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 204

def test_6_get_deleted_warehouse():
    response = requests.get(f"{BASE_URL}/api/v1/warehouses/99999/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 404

def test_7_get_all_warehouses():
    response = requests.get(f"{BASE_URL}/api/v1/warehouses/", headers={"Authorization": f"Bearer {API_KEY}"})
    assert response.status_code == 200
