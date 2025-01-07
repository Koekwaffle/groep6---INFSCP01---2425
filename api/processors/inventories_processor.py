
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
        query = "INSERT INTO inventories (item_id, quantity) VALUES (?, ?)"
        return self.execute(query, (inventory['item_id'], inventory['quantity']))

    def update(self, inventory_id, inventory):
        """Update an existing inventory."""
        query = "UPDATE inventories SET item_id = ?, quantity = ? WHERE id = ?"
        return self.execute(query, (inventory['item_id'], inventory['quantity'], inventory_id))

    def delete(self, inventory_id):
        """Delete an inventory by ID."""
        query = "DELETE FROM inventories WHERE id = ?"
        return self.execute(query, (inventory_id,))
