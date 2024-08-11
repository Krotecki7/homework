import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s: %(message)s',
                    filename='../logs/masks.log',
                    filemode='w', encoding='utf8')

masks_logger = logging.getLogger('masks')


def get_mask_card_number(card_number: str) -> str:
    """Функция маcкировки номера банковской карты"""
    masks_logger.info('Получаем данные карты')
    try:
        masks_logger.info('Маскируем карту')
        if card_number.isdigit() and len(card_number) == 16:
            return f"{card_number[:4]} {card_number[4:6]}{'*' * 2} {'*' * 4} {card_number[12:]}"
    except Exception as ex:
        masks_logger.error(f'Произошла ошибка: {ex}', exc_info=True)
        return "Неверный ввод"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки лицевого счета"""
    masks_logger.info('Получаем данные лицевого счета')
    try:
        masks_logger.info('Максируем номер лицевого счета')
        if account_number.isdigit() and len(account_number) == 20:
            return f"{'*' * 2}{account_number[16:]}"
    except Exception as ex:
        masks_logger.error(f'произошла ошибка: {ex}', exc_info=True)
        return 'Неверный ввод'


card_number = input("Введите номер карты: ")
account_number = input("Введите номер лицевого счета: ")


print(get_mask_card_number(card_number))
print(get_mask_account(account_number))
