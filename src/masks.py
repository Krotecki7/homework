import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

masks_logger = logging.getLogger("masks")
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s, %(name)s, %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str | str:
    """Функция маcкировки номера банковской карты"""
    masks_logger.info("Получаем данные карты")
    try:
        masks_logger.info("Маскируем карту")
        if card_number.isdigit() and len(card_number) == 16:
            return f"{card_number[:4]} {card_number[4:6]}{'*' * 2} {'*' * 4} {card_number[12:]}"
    except Exception as ex:
        masks_logger.error(f"Произошла ошибка: {ex}", exc_info=True)
        return "Неверный ввод"


def get_mask_account(account_number: str) -> str | str:
    """Функция маскировки лицевого счета"""
    masks_logger.info("Получаем данные лицевого счета")
    try:
        masks_logger.info("Максируем номер лицевого счета")
        if account_number.isdigit() and len(account_number) == 20:
            return f"{'*' * 2}{account_number[16:]}"
    except Exception as ex:
        masks_logger.error(f"произошла ошибка: {ex}", exc_info=True)
        return "Неверный ввод"


card_number = input("Введите номер карты: ")
account_number = input("Введите номер лицевого счета: ")


print(get_mask_card_number(card_number))
print(get_mask_account(account_number))
