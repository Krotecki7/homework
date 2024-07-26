from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """Декоратор, отлавливающий время начала и конца функции
    и выводящий результат в файл или консоль."""

    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write("my function ok.\n")
                else:
                    print("my function ok.")
            except Exception as e:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"my_function error: {e}. Inputs: {args}, {kwargs}")
                raise Exception(f"Ошибка: {e}")
            return result

        return wrapper

    return decorator


@log(filename="log.txt")
def my_func(x: int, y: int) -> float:
    """Функция деления чисел"""
    return x / y
