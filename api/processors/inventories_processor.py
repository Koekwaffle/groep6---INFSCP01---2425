
from providers.generic_functions_sqlite import GenericFunctionsSQLite

class Inventories_processor(GenericFunctionsSQLite):
    def get_all(self):
        """Retrieve all inventories."""
        query = "SELECT * FROM inventories"
        return self.fetch_all(query)

    def get(self, inventory_id):
        """Retrieve a single inventory by ID."""
        query = "SELECT * FROM inventories WHERE id = ?"
        return self.fetch_one(query, (inventory_id,))

    def create(self, inventory):
        """Add a new inventory."""
        query = "INSERT INTO inventories (item_id, description, item_reference, location_id, total_on_hand, total_expected, total_ordered, total_allocated, total_available) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        params = (inventory['item_id'], inventory['description'], inventory['item_reference'], inventory['location_id'], inventory['total_on_hand'], inventory['total_expected'], inventory['total_ordered'], inventory['total_allocated'], inventory['total_available'])
        return self.execute(query, params)

    def update(self, inventory_id, inventory):
        """Update an existing inventory."""
        query = "UPDATE inventories SET item_id = ?, description = ?, item_reference = ?, location_id = ?, total_on_hand = ?, total_expected = ?, total_ordered = ?, total_allocated = ?, total_available = ? WHERE id = ?"
        params = (inventory['item_id'], inventory['description'], inventory['item_reference'], inventory['location_id'], inventory['total_on_hand'], inventory['total_expected'], inventory['total_ordered'], inventory['total_allocated'], inventory['total_available'], inventory_id)
        return self.execute(query, params)

    def delete(self, inventory_id):
        """Delete an inventory by ID."""
        query = "DELETE FROM inventories WHERE id = ?"
        return self.execute(query, (inventory_id,))
