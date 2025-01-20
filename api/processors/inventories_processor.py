from providers.generic_functions_sqlite import GenericFunctionsSQLite
DB_PATH = './ILY.db'

from providers.generic_functions_sqlite import GenericFunctionsSQLite
DB_PATH = './ILY.db'

from processors.generic_functions import GenericFunctionsSQLite


class Inventories_processor(GenericFunctionsSQLite):

    def get_inventory_totals_for_item(self, item_id):
        result = {
            "total_expected": 0,
            "total_ordered": 0,
            "total_allocated": 0,
            "total_available": 0
        }
        for x in self.data:
            if x["item_id"] == item_id:
                result["total_expected"] += x["total_expected"]
                result["total_ordered"] += x["total_ordered"]
                result["total_allocated"] += x["total_allocated"]
                result["total_available"] += x["total_available"]
        return result
    
    def get_inventories_for_item(self, item_id):
        result = []
        for x in self.data:
            if x["item_id"] == item_id:
                result.append(x)
        return result