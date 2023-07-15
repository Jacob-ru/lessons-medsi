"""
В данном случае точкой входа в приложение будет вызов консольной команды
"""

import sys

from lesson1.shop.adapters import create_order_and_print_all
from lesson1.shop.entities import OrderItem

if __name__ == '__main__':
    user_id = int(sys.argv[1])

    items = [(1, 1, 500), (2, 5, 200)] # (ид_товара, количество, стоимость за единицу)

    create_order_and_print_all(user_id, items)