
from .base import Base

class OrderItems(Base):
    __tablename__ = "order_items"

    id: int
    order_id: int
    item_id: int
    amount: int
