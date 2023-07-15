"""

Модуль в котором хранятся DTO для обмена данными между системами

"""
from typing import List, Tuple


def example_1_calc_average_coordinate(points: List[Tuple[float, float]]):
    """
    Функция рассчитывает среднее значение широты и долготы для множества точек
    points - список кортежей из двух элементов в которых
    первый элемент - значение широты
    второй элемент - значение долготы
    """


def example_2_create_connection(username: str, password: str, host: str, port: int):
    """
    Формирует строку для подключения к базе данных
    """


class Point:
    def __init__(self, *, longitude: float, latitude: float):
        self.longitude = longitude
        self.latitude = latitude


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


def example_2_create_connection(username: str, password: str, host: str, port: int):
    """
    Формирует строку для подключения к базе данных
    """
