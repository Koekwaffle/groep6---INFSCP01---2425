
from .base import Base

class ShipmentItems(Base):
    __tablename__ = "shipment_items"

    id: int
    shipment_id: int
    item_id: int
    amount: int
