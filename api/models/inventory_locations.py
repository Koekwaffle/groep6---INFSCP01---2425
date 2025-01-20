
from .base import Base

class InventoryLocations(Base):
    __tablename__ = "inventory_locations"

    id: int
    inventory_id: int
    location_id: int
    quantity: int
