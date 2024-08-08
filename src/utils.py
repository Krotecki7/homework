import json
import os
from typing import Any

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")


def get_data(path_to_file: str) -> Any:
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []
