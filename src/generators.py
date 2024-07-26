from typing import Generator, Union


def filter_by_currency(transactions: list, currency: str = "USD") -> Union[Generator]:
    """Функция, которая принимает список словарей, представляющих транзакции.
    И поочередно выдает транзакции, где валюта соответствует заданной('currency')."""
#    for item in transactions:
    try:
        for value in transactions:
            if value["operationAmount"]["currency"]["name"] == currency:
                yield value
            else:
                raise StopIteration
    except StopIteration:
        print("Не найден currency")


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
