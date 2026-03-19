import pytest
import sys
from unittest.mock import patch
from src.cli import input


def test_no_arguments():
    with patch.object(sys, "argv", ["script_report"]):
        with pytest.raises(SystemExit):
            input()


def test_correct_flags():
    with patch.object(
        sys,
        "argv",
        ["script_report", "--files", "test.csv", "--report", "median-coffee"],
    ):
        args = input()
        assert args.files == ["test.csv"]
        assert args.report == "median-coffee"


def test_wrong_files_flag1():
    with patch.object(
        sys, "argv", ["script_report", "--file", "a.csv", "--report", "median-coffee"]
    ):
        with pytest.raises(SystemExit):
            input()


def test_wrong_files_flag2():
    with patch.object(
        sys, "argv", ["script_report", "-files", "a.csv", "--report", "median-coffee"]
    ):
        with pytest.raises(SystemExit):
            input()


def test_wrong_files_flag3():
    with patch.object(
        sys, "argv", ["script_report", "-f", "a.csv", "--report", "median-coffee"]
    ):
        with pytest.raises(SystemExit):
            input()


def test_wrong_files_flag4():
    with patch.object(
        sys, "argv", ["script_report", "--f", "a.csv", "--report", "median-coffee"]
    ):
        with pytest.raises(SystemExit):
            input()


def test_wrong_report_flag1():
    with patch.object(
        sys, "argv", ["script_report", "--files", "a.csv", "--rep", "median-coffee"]
    ):
        with pytest.raises(SystemExit):
            input()


def test_wrong_report_flag2():
    with patch.object(
        sys, "argv", ["script_report", "--files", "a.csv", "-report", "median-coffee"]
    ):
        with pytest.raises(SystemExit):
            input()


def test_wrong_report_flag3():
    with patch.object(
        sys, "argv", ["script_report", "--files", "a.csv", "--reports", "median-coffee"]
    ):
        with pytest.raises(SystemExit):
            input()


def test_wrong_report_flag4():
    with patch.object(
        sys, "argv", ["script_report", "--files", "a.csv", "-r", "median-coffee"]
    ):
        with pytest.raises(SystemExit):
            input()


def test_uppercase_flags():
    with patch.object(
        sys, "argv", ["script_report", "--FILES", "a.csv", "--REPORT", "median-coffee"]
    ):
        with pytest.raises(SystemExit):
            input()
