import pytest

from src.utils import get_data


def test_get_data_success() -> None:
    data = get_data("data/operations.json")
    assert isinstance(data, list)


def test_get_data_file_not_found() -> None:
    data = get_data("data/non_existent_file.json")
    assert data == []
