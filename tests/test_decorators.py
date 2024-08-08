import pytest
from src.decorators import my_func, log


def test_log_1():
    @log(filename="log.txt")
    def my_func(x, y):
        return x / y

    result = my_func(2, 1)
    assert result == 2.0


def test_log_2():
    with pytest.raises(Exception):
        my_func()


def test_log_3():
    my_func(2, 1)
    with open("log.txt", "r", encoding="utf-8") as file:
        log_content = file.read()
    assert "my function ok." in log_content
