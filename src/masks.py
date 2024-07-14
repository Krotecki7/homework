def get_mask_card_number(user_card: str) -> str | None:
    """Функция маcкировки номера банковской карты"""
    if user_card.isdigit() and len(user_card) == 16:
        return f"{user_card[:4]} {user_card[4:5]}{'*' * 2} {'*' * 4} {user_card[12:]}"
    else:
        return None


def get_mask_account(user_acc: str) -> str | None:
    """Функция маскировки лицевого счета"""
    if user_acc.isdigit() and len(user_acc) == 20:
        return f"{'*' * 2}{user_acc[16:]}"
    else:
        return None
