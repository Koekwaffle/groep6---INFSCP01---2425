import requests
import pytest
# Documentation: https://docs.python-requests.org

# TODO: replace with test server url
BASE_URL = "http://145.24.223.218:3000"
API_KEY = "a1b2c3d4e5"

# 1. What's the first test we should write?

# Hint: you already ran into this situation at the start of this project

# 2. How do we setup our API server in test mode?

# Hint: think in terms of scenario's

# 3. Which tests can we write and run to cover all functionality?

# TODO: work out individually before discussing in your team

##########################
### Client endpoint tests
##########################
def test_auth_get_Clients():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct omgaat met onbevoegde toegang tot het eindpunt /api/v1/Clients
#   Waarom test je dit? Dit is een belangrijke veiligheidsmaatregel om onbevoegde gebruikers te voorkomen dat ze clientgegevens kunnen bekijken of wijzigen.
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin je wilt controleren hoe de API reageert als onbevoegde toegang wordt geprobeerd. Het maakt deel uit van de Client endpoints testen en controleert de authenticatiemechanisme voor het endpoint /api/v1/Clients
    response = requests.get(f"{BASE_URL}/api/v1/Clients")
    assert response.status_code == 401  # Unauthorized

def test_post_new_client():
#   Wat test je? Deze functie test het aanmaken van een nieuwe klant via het POST-verzoek naar het eindpunt /api/v1/clients
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct nieuwe klanten kan toevoegen aan het systeem
#   Bij welk scenario hoort dit? Dit past in het scenario waarin een gebruiker een nieuwe klant wil toevoegen aan het systeem.
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
#   Wat test je? Deze functie test het ophalen van alle klanten via het GET-verzoek naar het eindpunt /api/v1/clients
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct alle klanten kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Dit past in het scenario waarin een gebruiker alle klanten wil bekijken.
    response = requests.get(f"{BASE_URL}/api/v1/clients", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_put_new_information_in_clients():
#   Wat test je? Deze functie test het updaten van een bestaande klant via het PUT-verzoek naar het eindpunt /api/v1/clients/{id}
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een bestaande klant kan updaten in het systeem
#   Bij welk scenario hoort dit? Dit past in het scenario waarin een gebruiker een specifieke klant wil updaten.
    data = {
        "id": 945,
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
    response = requests.put(f"{BASE_URL}/api/v1/clients/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200

def test_get_specific_client():
#   Wat test je? Deze functie test het ophalen van een specifieke klant via het GET-verzoek naar het eindpunt /api/v1/clients/{id}
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een specifieke klant kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Dit past in het scenario waarin een gebruiker een specifieke klant wil bekijken.
    response = requests.get(f"{BASE_URL}/api/v1/clients/945", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

###############################
### Inventories endpoint tests
###############################

def test_create_inventory():
#   Wat test je? Deze functie test het aanmaken van een nieuwe voorraad via het POST-verzoek naar het eindpunt /api/v1/inventories
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct nieuwe voorraad kan toevoegen aan het systeem
#   Bij welk scenario hoort dit? Dit past in het scenario waarin een gebruiker een nieuwe voorraad wil toevoegen aan het systeem.
    data = {
        "id":  999,
        "item_id": "P000002",
        "description": "New inventory item",
        "item_reference": "new-ref",
        "locations": [
            12345,
            67890
        ],
        "total_on_hand": 100,
        "total_expected": 0,
        "total_ordered": 20,
        "total_allocated": 10,
        "total_available": 90
    }
    response = requests.post(f"{BASE_URL}/api/v1/inventories", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201


def test_get_all_inventories():
#   Wat test je? Deze functie test het ophalen van alle voorraden via het GET-verzoek naar het eindpunt /api/v1/inventories
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct alle voorraden kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Dit past in het scenario waarin een gebruiker alle voorraden wil bekijken.
    response = requests.get(f"{BASE_URL}/api/v1/inventories", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_get_specific_inventory():
#   Wat test je? Deze functie test het ophalen van een specifieke voorraad via het GET-verzoek naar het eindpunt /api/v1/inventories/{id} 
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een specifieke voorraad kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Dit past in het scenario waarin een gebruiker een specifieke voorraad wil bekijken.
    response = requests.get(f"{BASE_URL}/api/v1/inventories/{999}", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_put_new_info_in_inventory():
#   Wat test je? Deze functie test het updaten van een bestaande voorraad via het PUT-verzoek naar het eindpunt /api/v1/inventories/{id}
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een bestaande voorraad kan updaten in het systeem
#   Bij welk scenario hoort dit? Dit past in het scenario waarin een gebruiker een bestaande voorraad wil updaten.
    data = {
        "id": 999,
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
    response = requests.put(f"{BASE_URL}/api/v1/inventories/{999}", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200


###############################
### Item_groups endpoint tests
###############################

def test_create_item_group():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een nieuwe itemgroep kan aanmaken via het POST-verzoek naar het eindpunt /api/v1/item_groups
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct nieuwe itemgroepen kan toevoegen aan het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een nieuwe itemgroep wil toevoegen aan het systeem
    data = {
        "id":  999,
        "name": "Funny",
        "description": "Open-architected tertiary contingency",
        "created_at": "1995-09-07 07:15:07",
        "updated_at": "1996-09-16 17:31:21"
    }
    response = requests.post(f"{BASE_URL}/api/v1/item_groups", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201


def test_get_all_item_groups():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct alle itemgroepen kan ophalen via het GET-verzoek naar het eindpunt /api/v1/item_groups
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct alle itemgroepen kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker alle itemgroepen wil bekijken
    response = requests.get(f"{BASE_URL}/api/v1/item_groups", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_get_specific_item_group():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een specifieke itemgroep kan ophalen via het GET-verzoek naar het eindpunt /api/v1/item_groups/{id}
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een specifieke itemgroep kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een specifieke itemgroep wil bekijken
    response = requests.get(f"{BASE_URL}/api/v1/item_groups/1", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_put_new_info_in_item_group():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een bestaande itemgroep kan updaten via het PUT-verzoek naar het eindpunt /api/v1/item_groups/{id}
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een bestaande itemgroep kan updaten in het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een bestaande itemgroep wil updaten
    data = {
        "id": 999,
        "name": "Updated Electronics",
        "description": "Updated description for the electronics group",
        "created_at": "1998-05-15 19:52:53",
        "updated_at": "2024-09-30 12:50:00"
    }
    response = requests.put(f"{BASE_URL}/api/v1/item_groups/0", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201


###############################
### Item_lines endpoint tests
###############################

def test_create_item_line():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een nieuwe itemline kan aanmaken via het POST-verzoek naar het eindpunt /api/v1/item_lines
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct nieuwe itemlines kan toevoegen aan het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een nieuwe itemline wil toevoegen aan het systeem
    data = {
        "id":  999,
        "name": "New Item Line",
        "description": "This is a new item line",
        "created_at": "1995-09-07 07:15:07",
        "updated_at": "1996-09-16 17:31:21"
    }
    response = requests.post(f"{BASE_URL}/api/v1/item_lines", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201


def test_get_all_item_lines():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct alle itemlines kan ophalen via het GET-verzoek naar het eindpunt /api/v1/item_lines
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct alle itemlines kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker alle itemlines wil bekijken
    response = requests.get(f"{BASE_URL}/api/v1/item_lines", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_get_specific_item_line():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een specifieke itemline kan ophalen via het GET-verzoek naar het eindpunt /api/v1/item_lines/{id}
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een specifieke itemline kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een specifieke itemline wil bekijken
    response = requests.get(f"{BASE_URL}/api/v1/item_lines/96", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_get_items_in_specific_item_line():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct de items van een specifieke itemline kan ophalen via het GET-verzoek naar het eindpunt /api/v1/item_lines/{id}/items
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct de items van een specifieke itemline kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker de items van een specifieke itemline wil bekijken
    response = requests.get(f"{BASE_URL}/api/v1/item_lines/96/items", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_put_new_info_in_item_line():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een bestaande itemline kan updaten via het PUT-verzoek naar het eindpunt /api/v1/item_lines/{id}
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een bestaande itemline kan updaten in het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een bestaande itemline wil updaten
    data = {
        "id": 999,
        "name": "Updated Item Line Name",
        "description": "Updated description for item line",
        "created_at": "2010-01-01 12:00:00",
        "updated_at": "2024-09-30 13:00:00"
    }
    response = requests.put(f"{BASE_URL}/api/v1/item_lines/96", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200




###############################
### Item_types endpoint tests
###############################

def test_create_item_type():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een nieuwe itemtype kan aanmaken via het POST-verzoek naar het eindpunt /api/v1/item_types
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct nieuwe itemtypes kan toevoegen aan het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een nieuw itemtype wil toevoegen aan het systeem
    data = {
        "id":  999,
        "name": "Tablet",
        "description": "don't know",
        "created_at": "1995-09-07 07:15:07",
        "updated_at": "1996-09-16 17:31:21"
    }
    response = requests.post(f"{BASE_URL}/api/v1/item_types", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201


def test_get_all_item_types():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct alle itemtypes kan ophalen via het GET-verzoek naar het eindpunt /api/v1/item_types
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct alle itemtypes kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker alle itemtypes wil bekijken
    response = requests.get(f"{BASE_URL}/api/v1/item_types", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_get_specific_item_type():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een specifieke itemtype kan ophalen via het GET-verzoek naar het eindpunt /api/v1/item_types/{id}
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een specifieke itemtype kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een specifieke itemtype wil bekijken
    response = requests.get(f"{BASE_URL}/api/v1/item_types/2", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_get_items_of_specific_item_type():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct de items van een specifieke itemtype kan ophalen via het GET-verzoek naar het eindpunt /api/v1/item_types/{id}/items
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct de items van een specifieke itemtype kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker de items van een specifieke itemtype wil bekijken
    response = requests.get(f"{BASE_URL}/api/v1/item_types/2/items", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_put_new_info_in_item_type():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een bestaande itemtype kan updaten via het PUT-verzoek naar het eindpunt /api/v1/item_types/{id}
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een bestaande itemtype kan updaten in het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een bestaande itemtype wil updaten
    data = {
        "id": 999,
        "name": "Updated Item Type Name",
        "description": "Updated description of the item type"
    }
    response = requests.put(f"{BASE_URL}/api/v1/item_types/2", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200


###############################
### Items endpoint tests
###############################

def test_create_item():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een nieuw item kan aanmaken via het POST-verzoek naar het eindpunt /api/v1/items
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct nieuwe items kan toevoegen aan het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een nieuw item wil toevoegen aan het systeem
    data = {
        "id": 999,
        "uid": "P000001",
        "code": "sjQ23408K",
        "description": "Face-to-face clear-thinking complexity",
        "short_description": "must",
        "upc_code": "6523540947122",
        "model_number": "63-OFFTq0T",
        "commodity_code": "oTo304",
        "item_line": 11,
        "item_group": 73,
        "item_type": 14,
        "unit_purchase_quantity": 47,
        "unit_order_quantity": 13,
        "pack_order_quantity": 11,
        "supplier_id": 34,
        "supplier_code": "SUP423",
        "supplier_part_number": "E-86805-uTM"
    }
    response = requests.post(f"{BASE_URL}/api/v1/items", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201


def test_get_all_items():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct alle items kan ophalen via het GET-verzoek naar het eindpunt /api/v1/items
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct alle items kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker alle items wil bekijken
    response = requests.get(f"{BASE_URL}/api/v1/items", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_get_specific_item():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een specifiek item kan ophalen via het GET-verzoek naar het eindpunt /api/v1/items/{id}
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een specifiek item kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een specifiek item wil bekijken
    response = requests.get(f"{BASE_URL}/api/v1/items/40", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_get_specific_item_inventory():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct de inventaris van een specifiek item kan ophalen via het GET-verzoek naar het eindpunt /api/v1/items/{id}/inventory
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct de inventaris van een specifiek item kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker de inventaris van een spec
    response = requests.get(f"{BASE_URL}/api/v1/item_types/2/items", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_get_specific_item_inventory_totals():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct de totaalwaarden van de inventaris van een specifiek item kan ophalen via het GET-verzoek naar het eindpunt /api/v1/items/{id}/inventory/totals
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct de totaalwaarden van de inventaris van een specifiek item kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker de totaalwaarden van de inventaris van een specifiek item wil bekijken.
    response = requests.get(f"{BASE_URL}/api/v1/items/9/inventory/totals", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_put_new_info_in_item():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een bestaand item kan updaten via het PUT-verzoek naar het eindpunt /api/v1/items/{id}
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een bestaand item kan updaten in het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een bestaand item wil updaten.
    data = {
        "id": 999,
        "name": "Updated Item Name",
        "item_type_id": 2,
        "description": "Updated description of the item",
        "price": 100.00,
        "quantity": 50
    }
    response = requests.put(f"{BASE_URL}/api/v1/items/40", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200



###############################
### Locations endpoint tests
###############################

def test_create_location():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een nieuwe locatie kan aanmaken via het POST-verzoek naar het eindpunt /api/v1/locations
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct nieuwe locaties kan toevoegen aan het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een nieuwe locatie wil toevoegen aan het systeem.
    data = {
        "id": 999,
        "warehouse_id": 1,
        "code": "A.1.1",
        "name": "Row: A, Rack: 1, Shelf: 1"
    }
    response = requests.post(f"{BASE_URL}/api/v1/locations", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201


def test_get_all_locations():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct alle locaties kan ophalen via het GET-verzoek naar het eindpunt /api/v1/locations
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct alle locaties kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker alle locaties wil bekijken.
    response = requests.get(f"{BASE_URL}/api/v1/locations", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_get_specific_location():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een specifieke locatie kan ophalen via het GET-verzoek naar het eindpunt /api/v1/locations/{id}
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een specifieke locatie kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een specifieke locatie wil bekijken.
    response = requests.get(f"{BASE_URL}/api/v1/locations/2", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_put_new_info_in_location():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een bestaande locatie kan updaten via het PUT-verzoek naar het eindpunt /api/v1/locations/{id}
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een bestaande locatie kan updaten in het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een bestaande locatie wil updaten.
    data = {
        "id": 999,
        "name": "Updated Location Name",
        "address": "123 Updated Street",
        "city": "Updated City",
        "province": "Updated Province",
        "country": "Updated Country"
    }
    response = requests.put(f"{BASE_URL}/api/v1/locations/2", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200  # This may need to be adjusted based on actual API behavior


###############################
### Suppliers endpoint tests
###############################

def test_create_supplier():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een nieuwe leverancier kan aanmaken via het POST-verzoek naar het eindpunt /api/v1/suppliers
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct nieuwe leveranciers kan toevoegen aan het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een nieuwe leverancier wil toevoegen aan het systeem.
    data = {
        "id": 999,
        "code": "SUP0002",
        "name": "Holden-Quinn",
        "address": "576 Christopher Roads",
        "address_extra": "Suite 072",
        "city": "Amberbury",
        "zip_code": "16105",
        "province": "Illinois",
        "country": "Saint Martin",
        "contact_name": "Kathleen Vincent",
        "phonenumber": "001-733-291-8848x3542",
        "reference": "H-SUP0002"
    }
    response = requests.post(f"{BASE_URL}/api/v1/suppliers", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201


def test_get_all_suppliers():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct alle leveranciers kan ophalen via het GET-verzoek naar het eindpunt /api/v1/suppliers
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct alle leveranciers kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker alle leveranciers wil bekijken.
    response = requests.get(f"{BASE_URL}/api/v1/suppliers", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_get_specific_supplier():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een specifieke leverancier kan ophalen via het GET-verzoek naar het eindpunt /api/v1/suppliers/{id}
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een specifieke leverancier kan ophalen uit het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een specifieke leverancier wil bekijken.
    response = requests.get(f"{BASE_URL}/api/v1/suppliers/2", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_update_supplier():
#   Wat test je? Deze functie test je omdat je wilt controleren of de API correct een bestaande leverancier kan updaten via het PUT-verzoek naar het eindpunt /api/v1/suppliers/{id}
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een bestaande leverancier kan updaten in het systeem
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een bestaande leverancier wil updaten.
    data = {
        "id": 999,
        "code": "SUP0002",
        "name": "Holden-Quinn",
        "address": "576 Christopher Roads",
        "address_extra": "Suite 072",
        "city": "Amberbury",
        "zip_code": "16105",
        "province": "Illinois",
        "country": "Saint Martin",
        "contact_name": "Kathleen Vincent",
        "phonenumber": "001-733-291-8848x3542",
        "reference": "H-SUP0002"
    }
    response = requests.put(f"{BASE_URL}/api/v1/suppliers/2", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200



###############################
### Transfers endpoint tests
###############################

def test_create_transfer():
#   Wat test je? Deze functie test of de API correct een nieuwe overboeking kan maken via het POST-verzoek naar het eindpunt /api/v1/transfers.
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een nieuwe overboeking kan maken in het systeem.
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een nieuwe overboeking wil maken.
    data = {
        "id": 999,
        "reference": "TR00001",
        "transfer_to": 9229,
        "transfer_status": "Completed",
        "items": [
            {
                "item_id": "P007435",
                "amount": 23
            }
        ]
    }
    response = requests.post(f"{BASE_URL}/api/v1/transfers", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201


def test_get_all_transfers():
#   Wat test je? Deze functie test of de API correct een bestaande overboeking kan ophalen via het GET-verzoek naar het eindpunt /api/v1/transfers/{id}.
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een bestaande overboeking kan ophalen uit het systeem.
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een bestaande overboeking wil bekijken.
    response = requests.get(f"{BASE_URL}/api/v1/transfers", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_get_specific_transfer():
#   Wat test je? Deze functie test of de API correct een bestaande overboeking kan updaten via het PUT-verzoek naar het eindpunt /api/v1/transfers/{id}.
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een bestaande overboeking kan updaten in het systeem.
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een bestaande overboeking wil updaten.
    response = requests.get(f"{BASE_URL}/api/v1/transfers/1", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_get_items_from_specific_transfer():
#   Wat test je? Deze functie test of de API correct een lijst van items kan ophalen die behoren tot een specifieke overboeking via het GET-verzoek naar het eindpunt /api/v1/transfers/{id}/items.
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een lijst van items kan ophalen die behoren tot een specifieke overboeking uit het systeem.
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een lijst van items wil bekijken die behoren tot een specifieke overboeking.
    response = requests.get(f"{BASE_URL}/api/v1/transfers/1/items", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_put_transfer():
#   Wat test je? Deze functie test of de API correct een bestaande overboeking kan updaten via het PUT-verzoek naar het eindpunt /api/v1/transfers/{id}.
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een bestaande overboeking kan updaten in het systeem.
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een bestaande overboeking wil updaten.
    data = {
        "id": 999,
        "reference": "TR00001",
        "transfer_from": None,
        "transfer_to": 9229,
        "transfer_status": "Completed",
        "created_at": "2000-03-11T13:11:14Z",
        "items": [
            {
                "item_id": "P007435",
                "amount": 23
            }
        ]
    }
    response = requests.put(f"{BASE_URL}/api/v1/transfers/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200


###############################
### Warehouses endpoint tests
###############################

def test_create_warehouse():
#   Wat test je? Deze functie test of de API correct een nieuwe magazijn kan maken via het POST-verzoek naar het eindpunt /api/v1/warehouses.
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een nieuwe magazijn kan maken in het systeem.
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een nieuwe magazijn wil maken.
    data = {
        "id": 999,
        "code": "YQZZNL56",
        "name": "Heemskerk cargo hub",
        "address": "Karlijndreef 281",
        "zip": "4002 AS",
        "city": "Heemskerk",
        "province": "Friesland",
        "country": "NL",
        "contact": {
            "name": "Fem Keijzer",
            "phone": "(078) 0013363",
            "email": "blamore@example.net"
        }
    }
    response = requests.post(f"{BASE_URL}/api/v1/warehouses", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 201


def test_get_all_warehouses():
#   Wat test je? Deze functie test of de API correct een bestaand magazijn kan ophalen via het GET-verzoek naar het eindpunt /api/v1/warehouses/{id}.
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een bestaand magazijn kan ophalen uit het systeem.
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een bestaand magazijn wil bekijken.
    response = requests.get(f"{BASE_URL}/api/v1/warehouses", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_get_specific_warehouse():
#   Wat test je? Deze functie test of de API correct een specifiek magazijn kan ophalen via het GET-verzoek naar het eindpunt /api/v1/warehouses/{id}.
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een specifiek magazijn kan ophalen uit het systeem.
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een specifiek magazijn wil bekijken.
    response = requests.get(f"{BASE_URL}/api/v1/warehouses/1", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_get_specific_warehouse_locations():
#   Wat test je? Deze functie test of de API correct een lijst van locaties kan ophalen die behoren tot een specifiek magazijn via het GET-verzoek naar het eindpunt /api/v1/warehouses/{id}/locations.
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een lijst van locaties kan ophalen die behoren tot een specifiek magazijn uit het systeem.
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een lijst van locaties wil bekijken die behoren tot een specifiek magazijn.
    response = requests.get(f"{BASE_URL}/api/v1/warehouses/1/locations", headers={"API_KEY": API_KEY})
    assert response.status_code == 200

def test_update_warehouse():
#   Wat test je? Deze functie test of de API correct een bestaand magazijn kan updaten via het PUT-verzoek naar het eindpunt /api/v1/warehouses/{id}.
#   Waarom test je dit? Het is belangrijk om te verifiëren of de API correct een bestaand magazijn kan updaten in het systeem.
#   Bij welk scenario hoort dit? Deze test past in het scenario waarin een gebruiker een bestaand magazijn wil updaten.
    data = {
        "id": 999,
        "code": "YQZZNL56",
        "name": "Heemskerk cargo hub",
        "address": "Karlijndreef 281",
        "zip": "4002 AS",
        "city": "Heemskerk",
        "province": "Friesland",
        "country": "NL",
        "contact": {
            "name": "Fem Keijzer",
            "phone": "(078) 0013363",
            "email": "blamore@example.net"
        }
    }
    response = requests.put(f"{BASE_URL}/api/v1/warehouses/1", headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)
    assert response.status_code == 200
