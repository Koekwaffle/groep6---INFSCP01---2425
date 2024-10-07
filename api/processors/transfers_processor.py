from api.processors.generic_functions import Generic_functions

class Transfers_processor(Generic_functions):
    def get_items_in_transfer(self, transfer_id):
        for x in self.data:
            if x["id"] == transfer_id:
                return x["items"]
        return None
    pass