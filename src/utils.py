import os

import re
import pandas as pd
from pandas import DataFrame
import json
import logging
import os
from typing import Any
from collections import Counter

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_file_path = os.path.abspath(rel_file_path)

utils_logger = logging.getLogger("utils")
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s, %(name)s, %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
path_to_csv_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
path_to_xlsx_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def get_data(path_to_file: str) -> Any:
    """Функция, считывающая JSON файл и возвращающая пустой список при ошибке чтения."""
    try:
        utils_logger.info(f"Открываем файл {path_to_file} для чтения")
        with open(path_to_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        utils_logger.error("Ошибка чтения")
        return []


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


def search_by_str(data: list[dict], search_str: str) -> list[dict]:
    """Фильтрация описаний операций по строке поиска"""
    filtered_transactions = []
    for transaction in data:
        if re.findall(search_str, str(transaction["description"]), flags=re.IGNORECASE):
            filtered_transactions.append(transaction)
    return filtered_transactions


def count_operations(data: list[dict], categories: list[str]) -> dict:
    """Функция для подсчета кол-ва операций в каждой категории """
    counted_categories = []
    for transactions in data:
        description = transactions.get('description')
        for category in categories:
            if re.findall(category, str(description), flags=re.IGNORECASE):
                counted_categories.append(category)
    return Counter(counted_categories)
