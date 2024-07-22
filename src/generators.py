def filter_by_currency(transactions: list, currency: str = 'USD'):
    """Функция, которая принимает список словарей, представляющих транзакции.
    И поочередно выдает транзакции, где валюта соответствует заданной('currency')."""
    for item in transactions:
        if item["operationAmount"]["currency"]["name"] == currency:
            yield item


def transaction_descriptions(transactions: list):
    """Генератор, который выдает описание каждой операции по очереди."""
    for item in transactions:
        yield item["description"]


def card_number_generator(start, stop):
    for i in range(start, stop + 1):
        card_number = str(i)
        while len(card_number) < 16:
            card_number = '0' + card_number
        formatted_card_number = f'{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}'
        yield formatted_card_number
