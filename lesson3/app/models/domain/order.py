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

    @property
    def is_correct(self):
        """
        Проверка что заказ можно оформить
        Для этого необходимо:
        1) Cреди товаров не должно быть товара с нулевой ценой или нулевым количеством
        2) Стоимость заказа ненулевая
        """
        for item in self.items:
            if item.price and item.item_id:
                continue
            else:
                return False
        return True
