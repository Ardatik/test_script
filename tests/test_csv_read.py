import pytest
from src.csv_handler import read_csv_file
from .generate_dataset import create_dataset


def test_csv_file_not_exist():
    file_path = "/home/user/Рабочий стол/empty.csv"
    with pytest.raises(FileNotFoundError) as exc_info:
        read_csv_file(file_path)
    assert "файл не найден" in str(exc_info.value)
    
def test_file_not_csv():
    invalid_path = "data.txt"
    with pytest.raises(ValueError) as exc_info:
        read_csv_file(invalid_path)
    assert "Файл должен быть в формате .csv" in str(exc_info.value)
    
def test_read_csv_file_valid(tmp_path):
    file_path = create_dataset(
        file_name="fake",
        num_students=30,
        days=7,
        file_dir=tmp_path
    )
    result = read_csv_file(str(file_path))
    assert len(result) == 210
    assert "student" in result[0]
    assert "coffee_spent" in result[0]