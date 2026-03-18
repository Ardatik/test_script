import argparse
import tabulate
from typing import List, Tuple


def input():
    parser = argparse.ArgumentParser(
        prog="script_report",
        description="Скрипт для генерации отчётов из csv файлов",
        allow_abbrev=False,
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Путь к одному или нескольким csv файлам.",
    )
    parser.add_argument("--report", required=True, help="Название отчёта")
    return parser.parse_args()


def output_report(rows: List[Tuple], headers: List[str]) -> str:
    return tabulate.tabulate(rows, headers=headers, tablefmt="grid")
