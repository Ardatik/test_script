import csv
from typing import List, Dict
from pathlib import Path


def read_csv_file(file_path: str) -> list[dict[str, str]]:
    path = Path(file_path)
    if path.suffix != ".csv":
        raise ValueError("Файл должен быть в формате .csv")
    if not path.exists():
        raise FileNotFoundError(f"файл не найден: {file_path}")
    with open(path, encoding="utf-8") as file:
        return list(csv.DictReader(file))


def read_csv_files(paths: List[str]) -> List[Dict[str, str]]:
    data = []
    for path in paths:
        data.extend(read_csv_file(path))
    return data
        
