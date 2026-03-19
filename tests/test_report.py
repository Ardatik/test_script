import pytest
from src.csv_handler import read_csv_file
from src.median_coffee import median_coffee_report
import csv


@pytest.fixture
def csv_data():
    data_to_csv = [
        [
            "student",
            "date",
            "coffee_spent",
            "sleep_hours",
            "study_hours",
            "mood",
            "exam",
        ],
        ["Иванов Иван", "2026-01-15", "500", "3", "12", "зомби", "Математика"],
        ["Иванов Иван", "2026-01-16", "350", "5.5", "11", "норм", "Математика"],
        ["Алексеев Петр", "2026-01-15", "200", "6.5", "10", "норм", "Математика"],
        ["Алексеев Петр", "2026-01-16", "0", "7.5", "9", "норм", "Математика"],
        ["Алексеев Петр", "2026-01-17", "300", "4.5", "12", "Зомби", "Математика"],
        ["Алексеев Петр", "2026-01-18", "400", "5.5", "7", "норм", "Математика"],
        ["Петров Илья", "2026-01-15", "200", "6.5", "8", "норм", "Математика"],
        ["Петров Илья", "2026-01-16", "550", "1", "3", "умер", "Математика"],
        ["Петров Илья", "2026-01-17", "200", "8.5", "8", "норм", "Математика"],
    ]
    return data_to_csv


@pytest.fixture
def temp_csv_file(tmp_path, csv_data):
    file_path = tmp_path / "test_data.csv"
    with open(file_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)
    return str(file_path)


@pytest.fixture
def expected_data():
    data_verify = [
        ("Иванов Иван", 425.0),
        ("Алексеев Петр", 250.0),
        ("Петров Илья", 200.0),
    ]
    return data_verify


def test_median_coffee_report(temp_csv_file, expected_data):
    data = read_csv_file(temp_csv_file)
    result = median_coffee_report(data)
    assert len(result) == len(expected_data)
    assert result == expected_data
