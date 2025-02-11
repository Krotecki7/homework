from unittest.mock import patch

import pandas as pd
import pytest

from src.read_data import get_data_from_csv, get_data_from_xlsx


def test_get_data_success() -> None:
    data = get_data_from_csv("data/transactions.csv")
    assert isinstance(data, list)


def test_get_data_file_not_found() -> None:
    data = get_data_from_csv("data/non_existent_file.csv")
    assert data == []


def test_get_data_success_1() -> None:
    data = get_data_from_xlsx("data/transactions_excel.xlsx")
    assert isinstance(data, list)


def test_get_data_file_not_found_1() -> None:
    data = get_data_from_xlsx("data/non_existent_file.xlsx")
    assert data == []


@pytest.fixture
def test_df() -> pd.DataFrame:
    test_dict = {
        "id": [650703.0, 3598919.0],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        "amount": [16210.0, 29740.0],
        "currency_name": ["Sol", "Peso"],
        "currency_code": ["PEN", "COP"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
        "description": ["Перевод организации", "Перевод с карты на карту"],
    }

    return pd.DataFrame(test_dict)


@patch("src.read_data.pd.read_csv")
def test_get_data_from_csv_1(mock_read, test_df):
    mock_read.return_value = test_df
    result = get_data_from_csv("../data/transactions.csv")
    expected = test_df.to_dict(orient="records")
    assert result == expected


@patch("src.read_data.pd.read_excel")
def test_get_data_from_xlsx_1(mock_read, test_df):
    mock_read.return_value = test_df
    result = get_data_from_xlsx("../data/transactions_excel.xlsx")
    expected = test_df.to_dict(orient="records")
    assert result == expected
