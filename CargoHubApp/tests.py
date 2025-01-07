import requests
import pytest
from dotenv import load_dotenv
import os


load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("API_KEY")

# TODO: replace with test server url   'http://localhost:8080'
TEST_SERVER_URL = 'http://localhost:8080'
BASE_URL = 'http://145.24.223.218:8080'


########################## 
### Client endpoint tests 
########################## 
def test_auth_get_clients(): 
    response = requests.get(f"{BASE_URL}/api/v1/clients") 
    assert response.status_code == 401  # Unauthorized 

def test_post_new_client(): 
    data = { 
        "id": 945, 
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
    response = requests.post(f"{BASE_URL}/api/v1/clients", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 201 

def test_get_all_clients(): 
    response = requests.get(f"{BASE_URL}/api/v1/clients", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_client(): 
    response = requests.get(f"{BASE_URL}/api/v1/clients/945", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_put_new_information_in_clients(): 
    data = { 
        "name": "Updated Client Name", 
        "address": "789 Updated Street", 
        "city": "Updated City", 
        "zip_code": "99999", 
        "province": "Updated Province", 
        "country": "United States", 
        "contact_name": "Updated Contact Name", 
        "contact_phone": "555-999-8888", 
        "contact_email": "updated.contact@example.com", 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/clients/945", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_client(): 
    response = requests.delete(f"{BASE_URL}/api/v1/clients/945", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204  # No Content

def test_post_client_with_invalid_data(): 
    data = { 
        "id": "invalid_id", 
        "name": "", 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/clients", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 400  # Bad Request

def test_put_client_with_invalid_data(): 
    data = { 
        "id": "invalid_id", 
        "name": "", 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/clients/945", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 400  # Bad Request

def test_delete_client_with_invalid_id(): 
    response = requests.delete(f"{BASE_URL}/api/v1/clients/invalid_id", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 404  # Not Found

############################### 
### Inventories endpoint tests 
############################### 
def test_create_inventory(): 
    data = { 
        "item_id": "P000002", 
        "description": "New inventory item", 
        "item_reference": "new-ref", 
        "locations": [12345, 67890], 
        "total_on_hand": 100, 
        "total_expected": 0, 
        "total_ordered": 20, 
        "total_allocated": 10, 
        "total_available": 90 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/inventories", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 201 

def test_get_all_inventories(): 
    response = requests.get(f"{BASE_URL}/api/v1/inventories", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_inventory(): 
    response = requests.get(f"{BASE_URL}/api/v1/inventories/P000002", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_update_inventory(): 
    data = { 
        "total_on_hand": 150, 
        "total_ordered": 30 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/inventories/P000002", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_inventory(): 
    response = requests.delete(f"{BASE_URL}/api/v1/inventories/P000002", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204  # No Content

############################### 
### Item Groups endpoint tests 
############################### 
def test_create_item_group(): 
    data = { 
        "name": "New Item Group", 
        "description": "Description of new item group" 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/item-groups", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 201 

def test_get_all_item_groups(): 
    response = requests.get(f"{BASE_URL}/api/v1/item-groups", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_item_group(): 
    response = requests.get(f"{BASE_URL}/api/v1/item-groups/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_update_item_group(): 
    data = { 
        "description": "Updated description" 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/item-groups/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_item_group(): 
    response = requests.delete(f"{BASE_URL}/api/v1/item-groups/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204  # No Content

############################### 
### Item Lines endpoint tests 
############################### 
def test_create_item_line(): 
    data = { 
        "item_id": "P000002", 
        "quantity": 10 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/item-lines", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 201 

def test_get_all_item_lines(): 
    response = requests.get(f"{BASE_URL}/api/v1/item-lines", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_item_line(): 
    response = requests.get(f"{BASE_URL}/api/v1/item-lines/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_update_item_line(): 
    data = { 
        "quantity": 15 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/item-lines/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_item_line(): 
    response = requests.delete(f"{BASE_URL}/api/v1/item-lines/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204  # No Content

############################### 
### Item Types endpoint tests 
############################### 
def test_create_item_type(): 
    data = { 
        "name": "New Item Type", 
        "description": "Description of new item type" 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/item-types", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 201 

def test_get_all_item_types(): 
    response = requests.get(f"{BASE_URL}/api/v1/item-types", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_item_type(): 
    response = requests.get(f"{BASE_URL}/api/v1/item-types/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_update_item_type(): 
    data = { 
        "description": "Updated description" 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/item-types/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_item_type(): 
    response = requests.delete(f"{BASE_URL}/api/v1/item-types/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204  # No Content

############################### 
### Items endpoint tests 
############################### 
def test_create_item(): 
    data = { 
        "name": "New Item", 
        "description": "Description of new item", 
        "item_type_id": 1 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/items", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 201 

def test_get_all_items(): 
    response = requests.get(f"{BASE_URL}/api/v1/items", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_item(): 
    response = requests.get(f"{BASE_URL}/api/v1/items/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_update_item(): 
    data = { 
        "description": "Updated item description" 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/items/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_item(): 
    response = requests.delete(f"{BASE_URL}/api/v1/items/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204  # No Content

############################### 
### Locations endpoint tests 
############################### 
def test_create_location(): 
    data = { 
        "name": "New Location", 
        "address": "123 New Location St", 
        "city": "New City", 
        "zip_code": "12345", 
        "province": "New Province", 
        "country": "New Country" 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/locations", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 201 

def test_get_all_locations(): 
    response = requests.get(f"{BASE_URL}/api/v1/locations", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_location(): 
    response = requests.get(f"{BASE_URL}/api/v1/locations/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_update_location(): 
    data = { 
        "address": "456 Updated Location St" 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/locations/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_location(): 
    response = requests.delete(f"{BASE_URL}/api/v1/locations/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204  # No Content

############################### 
### Suppliers endpoint tests 
############################### 
def test_create_supplier(): 
    data = { 
        "name": "New Supplier", 
        "contact_name": "Supplier Contact", 
        "contact_phone": "123-456-7890", 
        "contact_email": "supplier@example.com" 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/suppliers", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 201 

def test_get_all_suppliers(): 
    response = requests.get(f"{BASE_URL}/api/v1/suppliers", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_supplier(): 
    response = requests.get(f"{BASE_URL}/api/v1/suppliers/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_update_supplier(): 
    data = { 
        "contact_name": "Updated Supplier Contact" 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/suppliers/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_supplier(): 
    response = requests.delete(f"{BASE_URL}/api/v1/suppliers/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204  # No Content

############################### 
### Transfers endpoint tests 
############################### 
def test_create_transfer(): 
    data = { 
        "from_location_id": 1, 
        "to_location_id": 2, 
        "item_id": "P000002", 
        "quantity": 10 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/transfers", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 201 

def test_get_all_transfers(): 
    response = requests.get(f"{BASE_URL}/api/v1/transfers", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_transfer(): 
    response = requests.get(f"{BASE_URL}/api/v1/transfers/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_update_transfer(): 
    data = { 
        "quantity": 15 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/transfers/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_transfer(): 
    response = requests.delete(f"{BASE_URL}/api/v1/transfers/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204  # No Content

############################### 
### Warehouses endpoint tests 
############################### 
def test_create_warehouse(): 
    data = { 
        "name": "New Warehouse", 
        "address": "123 Warehouse St", 
        "city": "Warehouse City", 
        "zip_code": "54321", 
        "province": "Warehouse Province", 
        "country": "Warehouse Country" 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/warehouses", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 201 

def test_get_all_warehouses(): 
    response = requests.get(f"{BASE_URL}/api/v1/warehouses", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_warehouse(): 
    response = requests.get(f"{BASE_URL}/api/v1/warehouses/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_update_warehouse(): 
    data = { 
        "address": "456 Updated Warehouse St" 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/warehouses/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_warehouse(): 
    response = requests.delete(f"{BASE_URL}/api/v1/warehouses/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204  # No Content

############################### 
### Error Handling Tests 
############################### 
def test_unauthorized_access(): 
    response = requests.get(f"{BASE_URL}/api/v1/clients") 
    assert response.status_code == 401  # Unauthorized 

def test_not_found(): 
    response = requests.get(f"{BASE_URL}/api/v1/clients/99999", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 401  # Not Found 

def test_invalid_data(): 
    data = { 
        "name": "", 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/clients", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 500  # Bad Request 

def test_method_not_allowed(): 
    response = requests.put(f"{BASE_URL}/api/v1/clients", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 500  # Method Not Allowed 

def test_conflict(): 
    data = { 
        "id": 945, 
        "name": "Existing Client", 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/clients", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 500  # Conflict 

def test_internal_server_error(): 
    response = requests.get(f"{BASE_URL}/api/v1/clients/error") 
    assert response.status_code == 401  # Internal Server Error