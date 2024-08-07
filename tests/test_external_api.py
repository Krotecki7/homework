from unittest.mock import patch
import requests
from src.external_api import sum_transactions

transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }


@patch("requests.get")
def test_sum_transactions(mock_get):
    mock_get.return_value.json.return_value = ({"707025.257747"})
    assert sum_transactions(transaction) == 707025.257747
