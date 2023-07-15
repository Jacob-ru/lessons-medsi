from typing import List

from lesson1.shop.entities import Order


class OrdersRepoInterface:

    def add_order(self, order: Order):
        raise NotImplementedError

    def get_orders_for_user_id(self, user_id) -> List[Order]:
        raise NotImplementedError

    def get_order_by_id(self, order_id) -> Order:
        raise NotImplementedError


class NotifyClientInterface:
    def send_message_for_user(self, user_id: int, message: str):
        raise NotImplementedError
