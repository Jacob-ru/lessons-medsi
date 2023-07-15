
from pydantic import BaseModel
from typing import List, Optional


"""
{ // OrderRequest
  "items": [
      {
        // OrderRequestItem
        "item_id": 123, // !
        "quantity": 1, // !
        "price": 123 // !
      }
    ], 
  "phone": "8(999) 999-99-99" // Не обязательно (?)
}
"""

class OrderRequestItem(BaseModel):
    item_id: int
    quantity: int
    price: float


class OrderRequest(BaseModel):
    items: List[OrderRequestItem]
    phone: Optional[str]


"""
{ // CreatedOrderInfo
  "order_id": 'abcdef', // обязательно
  "total_sum": 123.123 // Обязательно
}
"""

class CreatedOrderInfo(BaseModel):
    order_id: str
    total_sum: float


"""
[
  { // PublicOrderInfo
     "order_id": 'abcdef', // !
     "total_sum": 123.123, // !
     "items": [
    { // OrderRequestItem
        "item_id": 123, // !
        "quantity": 1, // !
        "price": 123 // !
    },
  ]
  }
]
"""

class PublicOrderInfo(BaseModel):
    order_id: str
    total_sum: float
    items: List[OrderRequestItem]