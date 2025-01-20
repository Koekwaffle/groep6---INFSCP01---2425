from providers.generic_functions_sqlite import GenericFunctionsSQLite
DB_PATH = './ILY.db'

from providers.generic_functions_sqlite import GenericFunctionsSQLite
DB_PATH = './ILY.db'

from processors.generic_functions import GenericFunctionsSQLite

class Transfers_processor(GenericFunctionsSQLite):
    def get_items_in_transfer(self, transfer_id):
        for x in self.data:
            if x["id"] == transfer_id:
                return x["items"]
        return None
    pass