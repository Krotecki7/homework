import json
import logging
import os
from typing import Any

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


print(get_data(PATH_TO_FILE))