"""

Модуль в котором хранятся DTO для обмена данными между системами

"""
from typing import List, Tuple
import dataclasses

@dataclasses.dataclass
class Point:
    longitude: float
    latitude: float

points = [Point(longitude='sd', latitude=54.233334)]
print(points)

def example_1_calc_average_coordinate(points: List[Point]):
    """
    Функция рассчитывает среднее значение широты и долготы для множества точек
    points - список кортежей из двух элементов в которых
    первый элемент - значение широты
    второй элемент - значение долготы
    """
    if points:
        avg_longitude = sum(x.longitude for x in points) / len(points)
        avg_latitude = sum(x.latitude for x in points) / len(points)


example_1_calc_average_coordinate(points)

@dataclasses.dataclass
class DbConf:
    username: str
    password: str
    host: str
    port: int


def example_2_create_connection(config: DbConf):
    """
    Формирует строку для подключения к базе данных
    """
