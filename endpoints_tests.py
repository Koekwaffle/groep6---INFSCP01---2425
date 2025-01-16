import requests
import pytest

BASE_URL = 'http://127.0.0.1:8000'
API_KEY = "a1b2c3d4e5"

########################## 
### Client endpoint tests 
########################## 
def test_auth_get_clients(): 
    response = requests.get(f"{BASE_URL}/api/v1/clients/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 401  # Unauthorized 

def test_post_new_client(): 
    data = { 
        "name": "Nieuwe Klant", 
        "address": "1234 Nieuwe Straat", 
        "city": "Amsterdam", 
        "zip_code": "1234AB", 
        "province": "Noord-Holland", 
        "country": "Nederland", 
        "contact_name": "Jan Janssen", 
        "contact_phone": "06-12345678", 
        "contact_email": "nieuwe.klant@example.com" 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/clients/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 201 

def test_get_all_clients(): 
    response = requests.get(f"{BASE_URL}/api/v1/clients/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_client(): 
    response = requests.get(f"{BASE_URL}/api/v1/clients/1/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_put_new_information_in_clients(): 
    data = { 
        "id": 1,
        "name": "Updated Client Name", 
        "address": "789 Updated Street", 
        "city": "Updated City", 
        "zip_code": "99999", 
        "province": "Updated Province", 
        "country": "United States", 
        "contact_name": "Updated Contact Name", 
        "contact_phone": "555-999-8888", 
        "contact_email": "updated.contact@example.com", 
        "updated_at": "2024-09-30T14:21:34.248255Z"
    } 
    response = requests.put(f"{BASE_URL}/api/v1/clients/1/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_client(): 
    response = requests.delete(f"{BASE_URL}/api/v1/clients/9822/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204  # No Content

############################### 
### Inventories endpoint tests 
############################### 
def test_get_all_inventories(): 
    response = requests.get(f"{BASE_URL}/api/v1/inventories/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_inventory(): 
    response = requests.get(f"{BASE_URL}/api/v1/inventories/1/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_put_new_info_in_inventory(): 
    data = { 
        "id": 1,
        "item_id": "P000001",
        "description": "Updated description of the item",
        "item_reference": "sjQ23408K",
        "locations": [3211, 24700, 14123],
        "total_on_hand": 300,
        "total_expected": 50,
        "total_ordered": 120,
        "total_allocated": 60,
        "total_available": 180,
        "created_at": "2015-02-19 16:08:24",
        "updated_at": "2024-09-30 12:45:00"
    }
    response = requests.put(f"{BASE_URL}/api/v1/inventories/1/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_post_new_inventory(): 
    data = { 
        "item_id": "P990002",
        "description": "New inventory item",
        "item_reference": "new-ref",
        "locations": [12345, 67890],
        "total_on_hand": 100,
        "total_expected": 0,
        "total_ordered": 20,
        "total_allocated": 10,
        "total_available": 90
    }
    response = requests.post(f"{BASE_URL}/api/v1/inventories/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 201 

def test_delete_inventory(): 
    response = requests.delete(f"{BASE_URL}/api/v1/inventories/11721/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204  # No Content

############################### 
### Item Groups endpoint tests 
############################### 
def test_get_all_item_groups(): 
    response = requests.get(f"{BASE_URL}/api/v1/item_groups/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_item_group(): 
    response = requests.get(f"{BASE_URL}/api/v1/item_groups/1/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_put_new_info_in_item_group(): 
    data = { 
        "id": 0,
        "name": "Updated Electronics",
        "description": "Updated description for the electronics group",
        "created_at": "1998-05-15 19:52:53",
        "updated_at": "2024-09-30 12:50:00"
    }
    response = requests.put(f"{BASE_URL}/api/v1/item_groups/1/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_post_new_item_group(): 
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

def test_delete_item_group(): 
    response = requests.delete(f"{BASE_URL}/api/v1/item_groups/101/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204  # No Content

############################### 
### Item Lines endpoint tests 
############################### 
def test_get_all_item_lines(): 
    response = requests.get(f"{BASE_URL}/api/v1/item_lines/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_item_line(): 
    response = requests.get(f"{BASE_URL}/api/v1/item_lines/96/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_items_in_specific_item_line(): 
    response = requests.get(f"{BASE_URL}/api/v1/item_lines/96/items", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_put_new_info_in_item_line(): 
    data = { 
        "id": 96,
        "name": "Updated Item Line Name",
        "description": "Updated description for item line",
        "created_at": "2010-01-01 12:00:00",
        "updated_at": "2024-09-30 13:00:00"
    }
    response = requests.put(f"{BASE_URL}/api/v1/item_lines/96/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_post_new_item_line(): 
    data = { 
        "name": "New Item Line",
        "description": "This is a new item line"
    }
    response = requests.post(f"{BASE_URL}/api/v1/item_lines/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 201 

def test_delete_item_line(): 
    response = requests.delete(f"{BASE_URL}/api/v1/item_lines/97/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204  # No Content

############################### 
### Locations endpoint tests 
############################### 
def test_get_all_locations(): 
    response = requests.get(f"{BASE_URL}/api/v1/locations/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_location(): 
    response = requests.get(f"{BASE_URL}/api/v1/locations/2/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_put_new_info_in_location(): 
    data = { 
        "name": "Updated Location Name",
        "address": "123 Updated Street",
        "city": "Updated City",
        "province": "Updated Province",
        "country": "Updated Country"
    }
    response = requests.put(f"{BASE_URL}/api/v1/locations/2/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_post_new_location(): 
    data = { 
        "warehouse_id": 1,
        "code": "A.1.1",
        "name": "Row: A, Rack: 1, Shelf: 1"
    }
    response = requests.post(f"{BASE_URL}/api/v1/locations/", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 201 

def test_delete_location(): 
    response = requests.delete(f"{BASE_URL}/api/v1/locations/2/", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204  # No Content
