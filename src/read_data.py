import os

import pandas as pd
from pandas import DataFrame

path_to_csv_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
path_to_xlsx_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def get_data_from_csv(path_to_file: str) -> list:
    """Функция возвращает список словарей из csv-файла"""
    try:
        csv_data = pd.read_csv(path_to_file, delimiter=";")
        return csv_data.to_dict(orient='records')
    except FileNotFoundError:
        return []


def get_data_from_xlsx(path_to_file: str) -> list:
    """Функция возвращает список словарей из excel-файла"""
    try:
        excel_data = pd.read_excel(path_to_file)
        return excel_data.to_dict(orient='records')
    except FileNotFoundError:
        return []
