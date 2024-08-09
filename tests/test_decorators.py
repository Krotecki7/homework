from typing import Any

import pytest

from src.decorators import log, my_func


def test_log_1() -> None:
    @log(filename="log.txt")
    def my_func(x: int, y: int) -> Any:
        return x / y

    result = my_func(2, 1)
    assert result == 2.0


def test_log_2() -> None:
    with pytest.raises(Exception):
        my_func()


def test_log_3() -> None:
    my_func(2, 1)
    with open("log.txt", "r", encoding="utf-8") as file:
        log_content = file.read()
    assert "my function ok." in log_content
