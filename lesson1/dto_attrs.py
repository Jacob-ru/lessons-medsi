"""

Модуль в котором хранятся DTO для обмена данными между системами

"""
from typing import List, Tuple
from attrs import define, field


@define
class Point:
    longitude: float
    latitude: float


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


points = [Point(longitude=45.3222, latitude=54.233334)]
example_1_calc_average_coordinate(points)

@define
class DbConf:
    username: str
    password: str
    host: str
    port: int


def example_2_create_connection(config: DbConf):
    """
    Формирует строку для подключения к базе данных
    """
