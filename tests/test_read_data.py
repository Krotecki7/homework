import pytest
from pandas import DataFrame
from src.read_data import get_data_from_csv, get_data_from_xlsx


def test_get_data_success() -> None:
    data = get_data_from_csv("data/transactions.csv")
    assert isinstance(data, DataFrame)


def test_get_data_file_not_found() -> None:
    data = get_data_from_csv("data/non_existent_file.csv")
    assert data == FileNotFoundError(2, 'No such file or directory')


def test_get_data_success_1() -> None:
    data = get_data_from_xlsx("data/transactions.xlsx")
    assert isinstance(data, DataFrame)


def test_get_data_file_not_found_1() -> None:
    data = get_data_from_xlsx("data/non_existent_file.xlsx")
    assert data == FileNotFoundError(2, 'No such file or directory')
