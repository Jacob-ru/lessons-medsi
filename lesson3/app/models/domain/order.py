from pydantic import BaseModel, Field
from typing import List
from uuid import UUID, uuid4

class OrderItem(BaseModel):
    item_id: int
    quantity: int
    price: float


class Order(BaseModel):
    id: str = Field(default_factory=lambda : uuid4().hex)
    items: List[OrderItem]
    username: str

    @property
    def total_sum(self):
        return sum([x.price * x.quantity for x in self.items])
