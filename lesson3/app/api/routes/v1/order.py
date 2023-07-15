from typing import List

from fastapi import Depends

from app.api.dependencies.security import get_current_user
from app.models.schemas import order as order_schemas
from app.models.schemas.user import PublicUserInfo
from .routes import router


@router.post("/create_order", response_model=order_schemas.CreatedOrderInfo)
def create_order(data: order_schemas.OrderRequest, user: PublicUserInfo = Depends(get_current_user)):
    """Не реализуем никакой логики, а только возвращаем заглушку"""
    return order_schemas.CreatedOrderInfo(
        order_id=1,
        total_sum=123,
    )


@router.get("/orders_list", response_model=List[order_schemas.PublicOrderInfo])
def get_orders_list(user: PublicUserInfo = Depends(get_current_user)):
    """Не реализуем никакой логики, а только возвращаем заглушку"""
    return [
        order_schemas.PublicOrderInfo(
            order_id=1,
            total_sum=123,
            items=[
                order_schemas.OrderRequestItem(
                    item_id=123,
                    quantity=999,
                    price=33.33
                )
            ]
        )
    ]
