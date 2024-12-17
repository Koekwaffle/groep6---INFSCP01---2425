import requests
import pytest

# TODO: replace with test server url
BASE_URL = "http://145.24.223.218:8080"
API_KEY = "a1b2c3d4e5"

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
    response = requests.get(f"{BASE_URL}/api/v1/inventories/999", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_update_inventory(): 
    data = { 
        "item_id": "P000002", 
        "description": "Updated inventory item", 
        "item_reference": "updated-ref", 
        "locations": [12345, 67890], 
        "total_on_hand": 150, 
        "total_expected": 0, 
        "total_ordered": 30, 
        "total_allocated": 20, 
        "total_available": 130 } 
    response = requests.put(f"{BASE_URL}/api/v1/inventories/999", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_inventory(): 
    response = requests.delete(f"{BASE_URL}/api/v1/inventories/999", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204 

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
        "name": "Updated Item Group", 
        "description": "Updated description" 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/item-groups/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_item_group(): 
    response = requests.delete(f"{BASE_URL}/api/v1/item-groups/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204 

############################### 
### Item Lines endpoint tests 
############################### 

def test_create_item_line(): 
    data = { 
        "item_id": "P000003", 
        "description": "New item line" 
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
        "description": "Updated item line" 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/item-lines/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_item_line(): 
    response = requests.delete(f"{BASE_URL}/api/v1/item-lines/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204 

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
        "name": "Updated Item Type", 
        "description": "Updated description" 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/item-types/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_item_type(): 
    response = requests.delete(f"{BASE_URL}/api/v1/item-types/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204 

############################### 
### Items endpoint tests 
############################### 

def test_create_item(): 
    data = { 
        "item_id": "P000004", 
        "name": "New Item", 
        "description": "Description of new item" 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/items", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 201 

def test_get_all_items(): 
    response = requests.get(f"{BASE_URL}/api/v1/items", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_get_specific_item(): 
    response = requests.get(f"{BASE_URL}/api/v1/items/P000004", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 200 

def test_update_item(): 
    data = { 
        "name": "Updated Item", 
        "description": "Updated description" 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/items/P000004", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_item(): 
    response = requests.delete(f"{BASE_URL}/api/v1/items/P000004", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204 

############################### 
### Locations endpoint tests 
############################### 

def test_create_location(): 
    data = { 
        "name": "New Location", 
        "address": "123 Location St" 
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
        "name": "Updated Location", 
        "address": "456 Updated St" 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/locations/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_location(): 
    response = requests.delete(f"{BASE_URL}/api/v1/locations/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204 

############################### 
### Suppliers endpoint tests 
############################### 

def test_create_supplier(): 
    data = { 
        "name": "New Supplier", 
        "contact_info": "supplier@example.com" 
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
        "name": "Updated Supplier", 
        "contact_info": "updated.supplier@example.com" 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/suppliers/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_supplier(): 
    response = requests.delete(f"{BASE_URL }/api/v1/suppliers/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204 

############################### 
### Transfers endpoint tests 
############################### 

def test_create_transfer(): 
    data = { 
        "item_id": "P000005", 
        "from_location_id": 12345, 
        "to_location_id": 67890, 
        "quantity": 50 
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
        "quantity": 75 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/transfers/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_transfer(): 
    response = requests.delete(f"{BASE_URL}/api/v1/transfers/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204 

############################### 
### Warehouses endpoint tests 
############################### 

def test_create_warehouse(): 
    data = { 
        "name": "New Warehouse", 
        "address": "123 Warehouse St" 
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
        "name": "Updated Warehouse", 
        "address": "456 Updated St" 
    } 
    response = requests.put(f"{BASE_URL}/api/v1/warehouses/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 200 

def test_delete_warehouse(): 
    response = requests.delete(f"{BASE_URL}/api/v1/warehouses/1", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 204 

############################### 
### Error Handling Tests 
############################### 

def test_unauthorized_access(): 
    response = requests.get(f"{BASE_URL}/api/v1/clients ") 
    assert response.status_code == 401  # Unauthorized 

def test_not_found(): 
    response = requests.get(f"{BASE_URL}/api/v1/clients/99999", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 404  # Not Found 

def test_invalid_data(): 
    data = { 
        "id": "invalid_id",  # Invalid ID type 
        "name": "",  # Missing name 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/clients", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 400  # Bad Request 

def test_method_not_allowed(): 
    response = requests.put(f"{BASE_URL}/api/v1/clients", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 405  # Method Not Allowed 

def test_conflict(): 
    data = { 
        "id": 945, 
        "name": "Duplicate Client", 
        "address": "1234 Duplicate St", 
        "city": "Amsterdam", 
        "zip_code": "1234AB", 
        "province": "Noord-Holland", 
        "country": "Nederland", 
        "contact_name": "Jan Janssen", 
        "contact_phone": "06-12345678", 
        "contact_email": "duplicate.klant@example.com" 
    } 
    response = requests.post(f"{BASE_URL}/api/v1/clients", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data) 
    assert response.status_code == 409  # Conflict 

def test_internal_server_error(): 
    response = requests.get(f"{BASE_URL}/api/v1/clients/trigger-error", headers={"Authorization": f"Bearer {API_KEY}"}) 
    assert response.status_code == 500  # Internal Server Error 