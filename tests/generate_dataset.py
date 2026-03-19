from pathlib import Path

from faker import Faker
import csv
from datetime import datetime, timedelta
import random


def create_dataset(file_name, num_students = 30, days = 7, file_dir: str | None = None):
    fake = Faker("ru_RU")
    Faker.seed(42)
    random.seed(42)

    exams = ["Математика", "Физика", "Химия", "Информатика", "Биология"]
    moods = ["отл", "норм", "устал", "зомби", "не выжил"]
    start_date = datetime(2026, 1, 15)
    
    if file_dir:
        file_path = Path(file_dir) / f"{file_name}.csv"  
    else:
        Path(f"{file_name}.csv")

    with open(file_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "student",
                "date",
                "coffee_spent",
                "sleep_hours",
                "study_hours",
                "mood",
                "exam",
            ]
        )

        for _ in range(num_students):
            first_name = fake.first_name_male()
            last_name = fake.last_name_male()
            student_name = f"{first_name} {last_name}"

            for i in range(days):
                date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
                coffee_spent = str(random.randint(100, 700))
                sleep_hours = str(round(random.uniform(2.0, 10.0), 1))
                study_hours = str(random.randint(2, 18))
                mood = random.choice(moods)
                exam = random.choice(exams)
                writer.writerow(
                    [
                        student_name,
                        date,
                        coffee_spent,
                        sleep_hours,
                        study_hours,
                        mood,
                        exam,
                    ]
                )
    return str(file_path)