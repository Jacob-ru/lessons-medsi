"""
Бизнес сущности
"""
import uuid
from typing import List

from pydantic import BaseModel, Field


class OrderItem(BaseModel):
    name: str
    id: int
    price: float
    quantity: int


class Order(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    user_id: int
    items: List[OrderItem]
    total_price: float

    @property
    def total_price(self) -> float:
        return sum([x.price * x.quantity for x in self.items], 0.0)
