"""
Интеграционные тесты
Проверяют взаимную работу модулей приложения
"""
from unittest.mock import Mock

import pytest

from app.db.repositories.order import OrdersRepo
from app.db.repositories.order import OrdersRepo
from app.models.domain.order import Order, OrderItem
from app.services.order import check_and_create_order, IncorrectOrderError
from app.models.schemas.order import OrderRequest, OrderRequestItem


MOCKED_ORDER_ID = 123


def test_create_order(monkeypatch):
    """Тестируем взаимную работы репозитория, сервиса и доменной модели"""

    # Подменяем вызов OrdersRepo.create_order на обращение к заглушке, которая вернет заранее заданный идентификатор
    create_order_mock = Mock(return_value=MOCKED_ORDER_ID)
    monkeypatch.setattr(OrdersRepo, 'create_order', create_order_mock)
    order = OrderRequest(items=[OrderRequestItem(item_id=1, price=100, quantity=1)])

    created_order = check_and_create_order(order, 'test_username')

    assert create_order_mock.called
    assert created_order.order_id


def test_create_order_error(monkeypatch):
    """Заказ без товаров должен вызвать ошибку при проверке так как есть товар без стоимости"""

    # Подменяем вызов OrdersRepo.create_order на обращение к заглушке, которая вернет заранее заданный идентификатор
    create_order_mock = Mock(return_value=MOCKED_ORDER_ID)
    monkeypatch.setattr(OrdersRepo, 'create_order', create_order_mock)
    order = OrderRequest(items=[OrderRequestItem(item_id=1, price=0, quantity=1)])
    with pytest.raises(IncorrectOrderError):
        check_and_create_order(order, 'test_username')

    # проверим что при этом точно не было вызвано сохранение закза
    assert not create_order_mock.called



@pytest.fixture()
def prepare_db():
    """Подготовка базы для использования в тестах"""
    from app.main import app
    from app.main import init_mongo
    init_mongo(app)
    yield
    app.database['orders'].drop()

@pytest.fixture()
def add_orders_to_db(prepare_db):
    OrdersRepo().create_order(Order(username='test', items=[]))

def test_get_orders_list(prepare_db, add_orders_to_db):
    orders = OrdersRepo().get_orders('test')
    assert len(orders) == 1


def test_get_orders_list_case_2(prepare_db, add_orders_to_db):
    orders = OrdersRepo().get_orders('test')
    assert len(orders) == 1

