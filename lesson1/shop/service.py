from typing import List

from lesson1.shop.entities import Order, OrderItem
from lesson1.shop.impl import Repos, Clients


def get_user_orders(user_id: int) -> List[Order]:
    """Получение списка всех заказов по ид пользователя"""
    return Repos.orders_repo_impl().get_orders_for_user_id(user_id)


def create_order(user_id: int, items: List[OrderItem]) -> Order:
    """
    Создание заказа. После создания заказа отправляется уведомление пользователю
    """
    order = Order(
        user_id=user_id,
        items=items,
    )
    # Сохранение заказа
    Repos.orders_repo_impl().add_order(order)
    # Отправка уведомления
    Clients.notify_client_impl().send_message_for_user(order.user_id, "Заказ успешно оформлен")
    return order

