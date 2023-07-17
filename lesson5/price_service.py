from fastapi import FastAPI
from tracing import configure_tracing
import requests
from make_request import make_request
app = FastAPI()

configure_tracing(app, 'Сервис расчета стоимости')

# Цены товаров
ITEM_PRICES = {
    1: 100, # Товар с ид 1 имеет базовую стоимость 100
    2: 300,
    3: 455,
    4: 500,
}

@app.get("/get_item_price")
def get_final_item_price(item_id: int, username: str):
    """
    Определение стоимости заказа
    Логика определния стоимости:
    1) Берем базовую стоимость из ITEM_PRICES
    2) Из сервиса скидок определяем какой размер скидки у пользователя
    3) Пересчитываем стоимость исходя из базовой стоимости и размера скидки
    """

    # основноя стоимость товара
    base_item_price = ITEM_PRICES.get(item_id, 0)
    # размер скидки
    discount_size = make_request('get', 'http://localhost:8002/get_discount',
                                 params={'item_id': item_id},
                                 operation_name="Получение скидки")
    final_price = base_item_price * (1 - discount_size / 100)
    return final_price