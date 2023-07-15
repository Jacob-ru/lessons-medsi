from typing import Type

"""
Single Responsibility Principle (Принцип единственной ответственности)
"""

"""Пример реализации функциональности в одном классе"""
class Order:
    def create(self):
        """Создание заказа"""

    def notify_buyer(self, message):
        """Уведомление для покупателя"""


"""Пример с ограничением ответственности"""
class OrderRepo:
    def create(self, order):
        """Создание заказа"""

class Notifyer:
    def notify_buyer(self, order, message):
        """Уведомление для покупателя"""


"""
Open-Closed Principle (Принцип открытости-закрытости)
"""

class User:
    def __init__(self, name: str, type: str):
        self.type = type
        self.name = name

    def get_repr(self):
        if self.type == 'doctor':
            return f"Врач {self.name}"
        elif self.type == 'patient':
            return f"Пациент {self.name}"
        else:
            return f"Пользователь {self.name}"


class BasicUser:
    def __init__(self, name: str):
        self.name = name

    def get_repr(self):
        raise NotImplementedError


class User(BasicUser):
    def get_repr(self):
        return f"Пользователь {self.name}"


class Patient(BasicUser):
    def get_repr(self):
        return f"Пациент {self.name}"


class Doctor(BasicUser):
    def get_repr(self):
        return f"Врач {self.name}"


"""
Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
"""

class Order:
    def __init__(self, total_price: float):
        self.total_price = total_price

class DiscountedOrder(Order):
    def __init__(
            self, total_price: float, discount: float
    ):
        super().__init__(total_price)
        self.discount = discount

def get_orders_discount(orders):
    total_discount = 0
    for order in orders:
        if isinstance(order, DiscountedOrder):
            order_discount = order.discount
        else:
            order_discount = 0
        total_discount += order_discount



class Order:
    def __init__(self, total_price: float):
        self.total_price = total_price
        self.discount = 0

class DiscountedOrder(Order):
    def __init__(
            self, total_price: float, discount: float
    ):
        super().__init__(total_price)
        self.discount = discount

def get_orders_discount(orders):
    total_discount = 0
    for order in orders:
        order_discount = order.discount
        total_discount += order_discount



"""
Interface Segregation Principle (Принцип разделения интерфейса)
"""

"""Единый интерфейсе описывающий работу с базой данных"""
class DBInterface:
    def create_order(self):
        """Создание заказа"""
        raise NotImplementedError

    def create_user(self):
        """Создание пользователя"""
        raise NotImplementedError


"""Интерфейс разделен на два узкоспециализированных"""
class OrderDbInterface:
    def create_order(self):
        """Создание заказа"""
        raise NotImplementedError

class UserDbInterface:
    def create_user(self):
        """Создание пользователя"""
        raise NotImplementedError


"""
Dependency Inversion Principle (Принцип инверсии зависимостей)
"""
class config:
    DATABASE_TYPE = 'test'

def get_order(order_id):
    if config.DATABASE_TYPE == 'postgres':
        order = PostgresOrdersRepo.get_order_by_id(order_id)
    elif config.DATABASE_TYPE == 'mongodb':
        order = MongoDB.get_order_by_id(order_id)
    return order


class OrderRepoBase:
    def get_order_by_id(self, order_id):
        raise NotImplementedError


class PostgresDB(OrderRepoBase):
    """"""

class MongoDB(OrderRepoBase):
    """"""
    
def get_impl() -> OrderRepoBase:
    if config.DATABASE_TYPE == 'postgres':
        return PostgresDB()
    elif config.DATABASE_TYPE == 'mongodb':
        return MongoDB()


def get_order(order_id, repo: OrderRepoBase):
    return repo.get_order_by_id(order_id)
    return order

"""
>>> repo = get_impl()
>>> order = get_order(1, repo)
"""