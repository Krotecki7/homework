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


def test_log_3(capsys):

    my_func(2, 1)
    captured = capsys.readouterr()
    assert captured.out == ""
