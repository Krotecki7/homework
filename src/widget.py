from datetime import datetime

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(user_card: str) -> str | None:
    """Функция, обрабатывающая информацию о картах"""
    if "Счет" in user_card:
        account = user_card[-20:]
        return f"{user_card[:-20]} {get_mask_account(account)}"
    else:
        card_number = "".join(user_card[-16:].split())
        return f"{user_card[:-16]} {get_mask_card_number(card_number)}"


print(mask_account_card("Счет 64686473678894779589"))


def get_date(date_string: str) -> str:
    """Функция для возврата даты в привычном значении"""
    date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    return date.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))
