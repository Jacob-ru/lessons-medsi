from app.models.domain.order import Order
from typing import List

class OrdersRepo:

    @property
    def db(self):
        from app.main import app
        return app.database['orders']

    def create_order(self, order: Order) -> str:
        res = self.db.insert_one(order.dict())
        return res.inserted_id

    def log(self):
        """Какая-то очень сложная и тяделая функция"""
        pass

    def get_orders(self, username) -> List[Order]:
        self.log()
        return [Order(**x) for x in self.db.find({'username': username})]
