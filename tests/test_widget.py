import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('account_card, result',
                         [('Visa 7000792289606361', 'Visa 7000 79** **** 6361'),
                          ('Счет 73654108430135874305', 'Счет **4305'),
                          ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199')])
def test_mask_account_card(account_card: str, result: str) -> str:
    assert mask_account_card(account_card) == result


@pytest.fixture
def data():
    return '2024-03-11T02:26:18.671407'


def test_get_date(data: str) -> str:
    assert get_date(data) == '11.03.2024'

