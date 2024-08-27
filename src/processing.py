def filter_by_state(list_of_dict: list, state: str) -> list:
    """Функция фильтрует список словарей по указанному значению ключа 'state'. По умолчанию 'state'='EXECUTED'."""
    filtered_list = []
    for dict_item in list_of_dict:
        if dict_item.get('state') == state:
            filtered_list.append(dict_item)
    return filtered_list


def sort_by_date(dictionary: list, ascending: bool = True) -> list:
    """Фукция, возвращающая новый список словарей, отсортированный по дате.
    По умолчанию сортирует от более старой даты к новой"""
    sorted_dicts = sorted(dictionary, key=lambda x: x["date"], reverse=ascending)
    return sorted_dicts
