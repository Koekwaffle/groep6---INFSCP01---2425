from providers.generic_functions_sqlite import GenericFunctionsSQLite
DB_PATH = './ILY.db'

from providers.generic_functions_sqlite import GenericFunctionsSQLite
DB_PATH = './ILY.db'

from processors.generic_functions import GenericFunctionsSQLite

class Items_processor(GenericFunctionsSQLite):
    def get_items_for_item_line(self, item_line_id):
        result = []
        for x in self.data:
            if x["item_line"] == item_line_id:
                result.append(x)
        return result

    def get_items_for_item_group(self, item_group_id):
        result = []
        for x in self.data:
            if x["item_group"] == item_group_id:
                result.append(x)
        return result

    def get_items_for_item_type(self, item_type_id):
        result = []
        for x in self.data:
            if x["item_type"] == item_type_id:
                result.append(x)
        return result

    def get_items_for_supplier(self, supplier_id):
        result = []
        for x in self.data:
            if x["supplier_id"] == supplier_id:
                result.append(x)
        return result
    pass