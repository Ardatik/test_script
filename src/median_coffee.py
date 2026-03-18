from collections import defaultdict
from typing import List, Tuple
from src.stats import calculate_median


def median_coffee_report(csv_data: List[dict[str, str]]) -> List[Tuple[str, float]]:
    if not csv_data or len(csv_data) == 0:
        raise ValueError("Отсутствуют данные для подготовки отчёта")
    student_values = defaultdict(list)
    for row in csv_data:
        val = int(row["coffee_spent"])
        student_values[row["student"]].append(val)
    result = []
    for student, values in student_values.items():
        median = calculate_median(values)
        result.append((student, median))
    result.sort(key=lambda x: x[1], reverse=True)
    return result