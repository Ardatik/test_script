from src.csv_handler import read_csv_files
from src.cli import input, output_report
import src.report_handler as report_handler
import sys


def main():
    args = input()
    if args.report not in report_handler.reports:
        print(f"Отчёта '{args.report} не существует'.")
        sys.exit(1)
    try:
        data = read_csv_files(paths=args.files)
    except FileNotFoundError as e:
        print(f"Ошибка чтения файлов: {e}")
        sys.exit(1)
    report_func = report_handler.reports[args.report]["report"]
    headers = report_handler.reports[args.report]["headers"]
    rows = report_func(data)
    output = output_report(rows, headers)
    print(output)


if __name__ == "__main__":
    main()
