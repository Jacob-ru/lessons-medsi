from app.models.domain.order import Order
from typing import List

class OrdersRepo:
    def __init__(self):
        from app.main import app
        self.db = app.database['orders']

    def create_order(self, order: Order) -> str:
        res = self.db.insert_one(order.dict())
        return res.inserted_id

    def get_orders(self, username) -> List[Order]:
        return [Order(**x) for x in self.db.find({'username': username})]
