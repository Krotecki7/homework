import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def mask_card():
    return '7000792289606361'


def test_get_mask_card_number(mask_card: str) -> str | None:
    assert get_mask_card_number(mask_card) == '7000 79** **** 6361', "Неправильно набран номер"
    assert get_mask_card_number("") is None, "Введите номер карты"
    assert get_mask_card_number('1234556778991234324123134') is None, "Слишком длинный номер"
    assert get_mask_card_number('123455') is None, "Короткий номер"


@pytest.fixture
def mask_account():
    return '73654108430135874305'


def test_get_mask_account(mask_account: str) -> str | None:
    assert get_mask_account(mask_account) == '**4305', "Некорректный счет"
    assert get_mask_account('') is None, "Введите номер карты"
    assert get_mask_account('1234566787899121421553') is None, "Слишком длинный номер"
    assert get_mask_account('123445') is None, "Короткий номер"