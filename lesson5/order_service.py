from fastapi import FastAPI, HTTPException
from typing import List
from models import Order, OrderItem, CreateOrder
from tracing import configure_tracing
from make_request import make_request
import requests

app = FastAPI()

configure_tracing(app, 'Сервис Заказов')

@app.post("/create_order")
def create_order(data: CreateOrder):
    order_items = []

    # Пройдем в цикле по каждому товару из запроса
    for item_id in data.item_ids:
        # Определим стоимость товара для пользователя через сервис расчета цен
        item_final_price = make_request('get', 'http://localhost:8001/get_item_price',
                                        params={'item_id': item_id, 'username': data.username},
                                        operation_name="Расчет финальной стоимости заказа")
        # Создадим OrderItem (количество товара - 1 для всех)
        order_item = OrderItem(item_id=item_id, price=item_final_price, quantity=1)
        order_items.append(order_item)

    # Сформируем заказ
    order = Order(username=data.username,
                  items=order_items)
    if not order.is_correct:
        raise HTTPException(400, "Некорректный заказ!")

    save_order_in_db(order)
    return "Заказ создан"

def save_order_in_db(order):
    """Ничего не делаем"""