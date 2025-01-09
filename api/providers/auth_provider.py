
USERS = [
    {
        "api_key": "a1b2c3d4e5",
        "app": "CargoHUB Dashboard 1",
        "endpoint_access": {
            "full": True
        }
    },
    {
        "api_key": "KPtxcRZgO1fPYCp6iqqjciG8ER8QoqRd",
        "app": "Device_1_1",
        "endpoint_access": {
            # Example of restricting access to certain endpoints graag gedaan Tim
            "full": False,
            "warehouses": {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "locations":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "transfers":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "items":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "item_lines":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "item_groups":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "item_types":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "suppliers":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "orders":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "clients":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            },
            "shipments":  {
                "full": False,
                "get": True,
                "post": False,
                "put": False,
                "delete": False
            }
        }
    },
#Hier moet je de api key van de andere devices invullen 
# LET OP AI pakt maakt vaak eigen api keys aan. Gebruik degenen die in de db staan
#ALs je de api key van een device niet weet, kan je deze vinden in de database onder de tabel devices of 
# in de terminal als je transfer_data/API_keys.py runt. dat is makkelijker
]

_users = None

def init():
    global _users
    _users = USERS

def get_user(api_key):
    for x in _users:
        if x["api_key"] == api_key:
            return x
    return None

def has_access(user, path, method):
    access = user["endpoint_access"]
    if access["full"]:
        return True
    else:
        return access[path][method]