
from app.models.schemas import order as order_schemas
from app.db.repositories.order import OrdersRepo
from app.models.domain.order import OrderItem, Order


class IncorrectOrderError(Exception):
    pass

def check_and_create_order(data: order_schemas.OrderRequest, username: str):
    """
    Создание заказа с проверкой корректности
    Если заказ создать нельзя, вызывается исключение с наименованием ошибки
    """
    order = Order(
        username=username,
        items=[OrderItem(**x.dict()) for x in data.items]
    )

    if not order.is_correct:
        raise IncorrectOrderError("Нельзя создать заказ без товаров или с товарами без цены/количества")
    OrdersRepo().create_order(order=order)
    return order_schemas.CreatedOrderInfo(
        order_id=order.id,
        total_sum=order.total_sum,
    )