from app.models.domain.order import Order, OrderItem


def test_total_sum_case_1():
    """Заказ без товароd. Итоговая стоимость 0"""
    order = Order(
        username='test',
        items=[]
    )

    assert order.total_sum == 0


def test_total_sum_case_2():
    """
    Заказ с двумя товарам в одном экземпляре.
    Общая стоиомсть заказа должна быть суммой стоимости каждого товара
    """
    order = Order(
        username='test',
        items=[
            OrderItem(price=100, quantity=1, item_id=1),
            OrderItem(price=200, quantity=1, item_id=2)
        ]
    )

    assert order.total_sum == 300


# def test_total_sum_case_3():
#     """???"""


def test_order_is_correct_case_1():
    """В Заказе есть товары с ценами и количеством. Заказ корректен"""
    order = Order(
        username='test',
        items=[
            OrderItem(price=100, quantity=1, item_id=1),
            OrderItem(price=200, quantity=1, item_id=2)
        ]
    )

    assert order.is_correct


def test_order_is_correct_case_2():
    """В Заказе есть товары без цены. Заказ некорректен"""
    order = Order(
        username='test',
        items=[
            OrderItem(price=0, quantity=1, item_id=1),
            OrderItem(price=200, quantity=1, item_id=2)
        ]
    )

    assert not order.is_correct


def test_order_is_correct_case_3():
    """В заказе нет товаров. Заказ некорректен"""
    order = Order(
        username='test',
        items=[
        ]
    )

    assert not order.is_correct

