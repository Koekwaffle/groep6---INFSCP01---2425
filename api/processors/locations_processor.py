from providers.generic_functions_sqlite import GenericFunctionsSQLite
DB_PATH = './ILY.db'

from providers.generic_functions_sqlite import GenericFunctionsSQLite
DB_PATH = './ILY.db'

from processors.generic_functions import GenericFunctionsSQLite

class Locations_processor(GenericFunctionsSQLite):
    def get_items_in_order(self, order_id):
        for x in self.data:
            if x["id"] == order_id:
                return x["items"]
        return None

    def get_orders_in_shipment(self, shipment_id):
        result = []
        for x in self.data:
            if x["shipment_id"] == shipment_id:
                result.append(x["id"])
        return result

    def get_orders_for_client(self, client_id):
        result = []
        for x in self.data:
            if x["ship_to"] == client_id or x["bill_to"] == client_id:
                result.append(x)
        return result
    
    def get_locations_in_warehouse(self, warehouse_id):
        result = []
        for x in self.data:
            if x["warehouse_id"] == warehouse_id:
                result.append(x)
        return result
    pass