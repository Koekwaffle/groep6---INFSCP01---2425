from api.models.base import Base

class Orders(Base):
    def __init__(self):
        super().__init__()

    def gets(self):
        """Retrieve all orders."""
        query = "SELECT * FROM orders"
        return self.fetch_all(query)

    def get_order(self, order_id):
        """Retrieve a single order by ID."""
        query = "SELECT * FROM orders WHERE id = ?"
        return self.fetch_one(query, (order_id,))

    def get_items_in_order(self, order_id):
        """Retrieve items in a specific order."""
        query = "SELECT * FROM order_items WHERE order_id = ?"
        return self.fetch_all(query, (order_id,))

    def get_orders_in_shipment(self, shipment_id):
        """Retrieve all orders in a specific shipment."""
        query = "SELECT id FROM orders WHERE shipment_id = ?"
        return [row[0] for row in self.fetch_all(query, (shipment_id,))]

    def get_orders_for_client(self, client_id):
        """Retrieve all orders for a specific client."""
        query = "SELECT * FROM orders WHERE ship_to = ? OR bill_to = ?"
        return self.fetch_all(query, (client_id, client_id))

    def add_order(self, order):
        """Add a new order."""
        query = """
        INSERT INTO orders (shipment_id, ship_to, bill_to, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?)
        """
        timestamp = self.get_timestamp()
        params = (
            order['shipment_id'],
            order['ship_to'],
            order['bill_to'],
            timestamp,
            timestamp
        )
        self.execute_query(query, params)

    def update_order(self, order_id, order):
        """Update an existing order."""
        query = """
        UPDATE orders
        SET shipment_id = ?, ship_to = ?, bill_to = ?, updated_at = ?
        WHERE id = ?
        """
        params = (
            order['shipment_id'],
            order['ship_to'],
            order['bill_to'],
            self.get_timestamp(),
            order_id
        )
        self.execute_query(query, params)

    def remove_order(self, order_id):
        """Remove an order by ID."""
        query = "DELETE FROM orders WHERE id = ?"
        self.execute_query(query, (order_id,))

