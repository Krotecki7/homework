from typing import Generator, Union


def filter_by_currency(transactions: list, currency: str = "USD") -> list:
    """Функция, которая принимает список словарей, представляющих транзакции.
    И поочередно выдает транзакции, где валюта соответствует заданной('currency')."""
    filtered_transactions = []
    for value in transactions:
        if value.get("operationAmount") is not None:
            if value["operationAmount"]["currency"]["code"] == currency:
                filtered_transactions.append(value)
        else:
            if value.get("currency_code") == currency:
                filtered_transactions.append(value)
    return filtered_transactions


def transaction_descriptions(transactions: list) -> Union[Generator]:
    """Генератор, который выдает описание каждой операции по очереди."""
    for item in transactions:
        yield item["description"]


def card_number_generator(start: int, stop: int) -> Union[Generator]:
    """Генаратор выдачи номеров банковских карт в формате XXXX XXXX XXXX XXXX"""
    for i in range(start, stop + 1):
        card_number = str(i)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        yield formatted_card_number
