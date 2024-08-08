import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def sum_transactions(transaction: dict) -> Any:
    """Функция, которая принимает на вход транзакцию и возвращает сумму из нее"""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        result = response.json()
        return result["result"]
