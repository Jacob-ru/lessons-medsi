from typing import List

from fastapi import Depends

from app.api.dependencies.security import get_current_user
from app.models.schemas import order as order_schemas
from app.models.schemas.user import PublicUserInfo
from app.db.repositories.order import OrdersRepo
from app.models.domain.order import OrderItem, Order
from .routes import router


@router.post("/create_order", response_model=order_schemas.CreatedOrderInfo)
def create_order(data: order_schemas.OrderRequest, user: PublicUserInfo = Depends(get_current_user)):
    """Не реализуем никакой логики, а только возвращаем заглушку"""
    order = Order(
        username=user.username,
        items=[OrderItem(**x.dict()) for x in data.items]
    )
    OrdersRepo().create_order(order=order)
    return order_schemas.CreatedOrderInfo(
        order_id=order.id,
        total_sum=order.total_sum,
    )


@router.get("/orders_list", response_model=List[order_schemas.PublicOrderInfo])
def get_orders_list(user: PublicUserInfo = Depends(get_current_user)):
    """Не реализуем никакой логики, а только возвращаем заглушку"""
    orders = list(OrdersRepo().get_orders(user.username))
    return [
        order_schemas.PublicOrderInfo(
            order_id=order.id,
            total_sum=order.total_sum,
            items=[
                order_schemas.OrderRequestItem(
                    **item.dict()
                ) for item in order.items
            ]
        ) for order in orders
    ]
