import os
from typing import Any
from unittest.mock import patch

import pytest

from src.external_api import sum_transactions

api_key = os.getenv("API_KEY")


@pytest.fixture
def transaction() -> dict:
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_sum_transaction_2(transaction: dict) -> Any:
    assert sum_transactions(transaction) == 31957.58


@patch("requests.get")
def test_sum_transactions_1(mock_get: Any) -> Any:
    mock_get.return_value.json.return_value = {"result": 100.0}
    assert sum_transactions({"operationAmount": {"amount": 100, "currency": {"code": "test"}}}) == 100.0
    mock_get.assert_called_once()
