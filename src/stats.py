import statistics
from typing import List


def calculate_median(values_list: List) -> int | float:
    if len(values_list) == 0:
        raise ValueError("Отсутсвуют значения для вычисления медианы")
    return statistics.median(values_list)
