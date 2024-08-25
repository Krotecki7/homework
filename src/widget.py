from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_card: str) -> str | None:
    """Функция получает номер счета или название и номер карты, и возвращает их в замаскированном виде."""
    if "Счет" in user_card:
        account = user_card[-20:]
        return f"{user_card[:-20]}{get_mask_account(account)}"
    else:
        card_number = "".join(user_card[-16:].split())
        return f"{user_card[:-16]}{get_mask_card_number(card_number)}"


def get_date(date_string: str) -> str | None:
    """Функция для возврата даты в привычном значении (день, месяц, год) из получаемой строки"""
    date = (datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f") or
            datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ"))
    return date.strftime("%d.%m.%Y")
