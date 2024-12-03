
from .base import Base

class TransferItems(Base):
    __tablename__ = "transfer_items"

    id: int
    transfer_id: int
    item_id: int
    amount: int
