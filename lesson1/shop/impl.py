
from typing import Type

from lesson1.shop.interface import OrdersRepoInterface, NotifyClientInterface


class Repos:
    orders_repo_impl: Type[OrdersRepoInterface] = None


class Clients:
    notify_client_impl: Type[NotifyClientInterface] = None