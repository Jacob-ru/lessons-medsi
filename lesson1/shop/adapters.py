from typing import List, Tuple, Literal

from lesson1.shop.entities import Order, OrderItem
from lesson1.shop.impl import Repos, Clients
from lesson1.shop.interface import OrdersRepoInterface, NotifyClientInterface
from lesson1.shop.service import get_user_orders,create_order


def create_order_and_print_all(user_id, items: List[Tuple[int, int, float]]):
    """Создание заказа с печатью в консоль информации обо всех имеющихся у пользователя заказах"""
    order_items = [
        OrderItem(id=item_id,
                  name=f"Товар {item_id}",
                  quantity=quantity,
                  price=price) for item_id, quantity, price in items
    ]
    print(f"Creating order for{user_id=}")
    create_order(user_id, order_items)
    print("Getting orders list")
    orders = get_user_orders(user_id)
    print(f"orders count: {len(orders)}")
    for order in orders:
        print(order)


class OrdersRepo(OrdersRepoInterface):
    data = {}

    def add_order(self, order: Order):
        self.data[order.id] = order

    def get_order_by_id(self, order_id) -> Order:
        return self.data[order_id]

    def get_orders_for_user_id(self, user_id) -> List[Order]:
        orders = [x for x in self.data.values() if x.user_id == user_id]
        return orders



class NotifyClient(NotifyClientInterface):
    def send_message_for_user(self, user_id: int, message: str):
        print(f"""### SENDING EMAIL TO USER {user_id} WITH MESSAGE {message}""")


Repos.orders_repo_impl = OrdersRepo
Clients.notify_client_impl = NotifyClient

