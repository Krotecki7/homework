from typing import Any

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import (
    PATH_TO_FILE,
    get_data,
    get_data_from_csv,
    get_data_from_xlsx,
    path_to_csv_file,
    path_to_xlsx_file,
    search_by_str,
)
from src.widget import get_date, mask_account_card


def main() -> Any:
    print(
        """Привет! Добро пожаловать в программу работы
c банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )
    welcome_input = input()
    if welcome_input == "1":
        print("Для обработки выбран JSON файл.")
        data = get_data(PATH_TO_FILE)
    elif welcome_input == "2":
        print("Для Обработки выбран CSV файл.")
        data = get_data_from_csv(path_to_csv_file)
    elif welcome_input == "3":
        print("Для обработки выбран EXCEL файл.")
        data = get_data_from_xlsx(path_to_xlsx_file)

    state_message = """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:\n"""
    state = input(f"{state_message}\n").upper()
    while state not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции {state} недоступен.\n {state_message}")
        state = input().upper()
        if state in ["EXECUTED", "CANCELED", "PENDING"]:
            break
    filtered_data = filter_by_state(data, state)

    sort_data = input("Отсортировать операции по дате? Да/Нет\n").lower()
    if sort_data == "да":
        sort_data_up_or_low = input("Отсортировать по возрастанию или по убыванию?\n").lower()
        if sort_data_up_or_low == "по возрастанию":
            sorted_filtered_data = sort_by_date(filtered_data, ascending=False)
        elif sort_data_up_or_low == "по убыванию":
            sorted_filtered_data = sort_by_date(filtered_data, ascending=True)
    elif sort_data == "нет":
        sorted_filtered_data = filtered_data
    print(sorted_filtered_data)
    rub_transactions = input("Выводить только рублевые тразакции? Да/Нет\n").lower()
    if rub_transactions == "да":
        sorted_data_by_rub = filter_by_currency(sorted_filtered_data, "RUB")
    elif rub_transactions == "нет":
        sorted_data_by_rub = sorted_filtered_data

    filter_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
    if filter_description == "да":
        search_str = input("Введите слово или фразу для поиска:\n")
        new_filtered_data = search_by_str(sorted_data_by_rub, search_str)
    elif filter_description == "нет":
        new_filtered_data = sorted_data_by_rub

    print("Распечатываю итоговый список транзакций...")
    if len(new_filtered_data) > 0:
        print(f"Всего банковских операций в выборке: {len(new_filtered_data)}")
        for value in new_filtered_data:
            if value.get("description") == "Открытие вклада":
                print(
                    f"""{get_date(value.get('date'))} {value.get('description')}
{mask_account_card(value.get('to'))}
Сумма: {value["operationAmount"]["amount"] or value.get('amount')}
{value["operationAmount"]["currency"]["name"] or value.get('currency_name')}"""
                )
            else:
                print(
                    f"""{get_date(value.get('date'))} {value.get('description')}
{mask_account_card(value.get('from'))} -> {mask_account_card(value.get('to'))}
Сумма: {value["operationAmount"]["amount"] or value.get('amount')}
{value["operationAmount"]["currency"]["name"] or value.get('currency_name')}"""
                )
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
