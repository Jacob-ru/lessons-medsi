from pydantic import BaseModel

from fastapi import FastAPI
from tracing import configure_tracing
import requests

app = FastAPI()

configure_tracing(app, 'Сервис скидок')

# Цены товаров
ITEM_DISCOUNT = {
    1: 10, # товар 1 имеет скидку 10%
    2: 100,
    3: 25,
}

@app.get("/get_discount")
def get_final_item_price(item_id: int):
    """
    Определение размера скидки для пользователя
    """
    return ITEM_DISCOUNT[item_id]