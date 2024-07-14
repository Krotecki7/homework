def filter_by_state(dictionary: list, state="EXECUTED") -> list:
    """Функция, которая возвращает новый словарь по заданному ключу"""
    new_dict = []
    for member in dictionary:
        if member["state"] == state:
            new_dict.append(member)
    return new_dict
