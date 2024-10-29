# Задание 1. Как дела?
# Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он
# написал надоедливый декоратор, который при вызове декорируемой функции
# спрашивает у пользователя «Как дела?», вне зависимости от ответа пишет что-то
# вроде «А у меня не очень!» и только потом запускает саму функцию. Правда, после
# такой выходки Васю чуть не уволили с работы.
# Реализуйте такой же декоратор и проверьте его работу на нескольких функциях.

# from functools import wraps
# from typing import Callable, Any
#
#
# def how_are_you(func: Callable[..., Any]) -> Callable[..., Any]:
#     """
#     Декоратор, который спрашивает у пользователя 'Как дела?' и
#     выводит
#     предопределенное сообщение перед вызовом декорируемой функции.
#     """
#
#     @wraps(func)
#     def wrapper(*args: Any, **kwargs: Any) -> Any:
#         """
#         Функция-обертка, которая выполняет дополнительное поведение
#         перед вызовом декорируемой функции.
#         """
#         input('Как дела? ')  # Запрашиваем ответ у пользователя
#         print('А у меня не очень! Ладно, держи свою функцию.')  # Выводим сообщение
#         result = func(*args, **kwargs)  # Вызов оригинальной функции
#         return result
#
#     return wrapper
#
#
# @how_are_you
# def test() -> None:
#     """
#     Проверка декоратора и вывод простого сообщения.
#     """
#     print('<Тут что-то происходит...>')
#
#
# @how_are_you
# def another_function() -> None:
#     """
#     Еще один пример функции для проверки декоратора.
#     """
#     print('Еще один тестовый вывод.')
#
#
# if __name__ == "__main__":
#     test()  # Проверка декоратора на функции
# another_function()


# Задача 2. Замедление кода
# В программировании иногда возникает ситуация, когда работу функции нужно
# замедлить. Типичный пример — функция, которая постоянно проверяет,
# изменились ли данные на веб-странице или её код.
# Реализуйте декоратор, который перед выполнением декорируемой функции
# ждёт несколько секунд.

# from functools import wraps
# from time import sleep
# from typing import Callable, Any
#
#
# def slowdown_2s(func: Callable[..., Any]) -> Callable[..., Any]:
#
#
#     """
#     Декоратор для замедления работы функции на 2 секунды.
#     :param func: Декорируемая функция
#     :return: Функция-обертка
#     """
#
#
#     @wraps(func)
#     def wrapper(*args: Any, **kwargs: Any) -> Any:
#
#
#         """
#         Функция-обертка, которая приостанавливает выполнение на 2
#         секунды.
#         :param args: Позиционные аргументы
#         :param kwargs: Именованные аргументы
#         :return: Результат выполнения декорируемой функции
#         """
#         sleep(2)  # Приостановка выполнения на 2 секунды
#         result = func(*args, **kwargs)  # Вызов оригинальной функции
#         return result
#     return wrapper
#
#
# @slowdown_2s
# def test() -> None:
#
#
#     """
#     Проверка декоратора и вывод простого сообщения.
#     :return: None
#     """
#     print('<Тут что-то происходит...>')
#
#
# @slowdown_2s
# def another_function() -> None:
#
#
#     """
#     Еще один пример функции для проверки декоратора.
#     :return: None
#     """
#     print('Еще один тестовый вывод.')
#
# if __name__ == "__main__":
#     test()  # Ожидайте задержку 2 секунды перед выводом сообщения
# another_function()  # Ожидайте задержку 2 секунды перед выводом сообщения


# Задача 3. Счётчик
# Реализуйте декоратор counter, считающий и выводящий количество вызовов
# декорируемой функции.
# Для решения задачи нельзя использовать операторы global и nonlocal.

# from functools import wraps
# from typing import Callable, Any, Optional
#
#
# def counter(func: Callable) -> Callable:
#     """
#     Декоратор для подсчета количества вызовов функции.
#     :param func: Декорируемая функция.
#     :return: Обертка функции с подсчетом вызовов.
#     """
#
#     @wraps(func)
#     def wrapper(*args, **kwargs) -> Any:
#         """
#         Функция-обертка для увеличения и вывода счётчика вызовов
#         функции.
#         :param args: Позиционные аргументы декорируемой функции.
#         :param kwargs: Именованные аргументы декорируемой функции.
#         :return: Результат вызова декорируемой функции.
#         """
#         wrapper.count += 1  # Увеличиваем счетчик вызовов на единицу.
#         result = func(*args, **kwargs)  # Вызываем оригинальную функцию.
#         print(f"Функцию '{func.__name__}' вызвали {wrapper.count} раз")
#         # Выводим количество вызовов.
#         return result  # Возвращаем результат вызова оригинальной функции.
#
#     wrapper.count = 0  # Инициализируем счетчик вызовов.
#     return wrapper  # Возвращаем обертку.
#
#
# @counter
# def greeting(name: str, age: Optional[int] = None) -> str:
#     """
#     Приветствие с возрастом и именем.
#     :param name: Имя человека.
#     :param age: Возраст человека (по умолчанию None).
#     :return: Строка с приветствием.
#     """
#     if age:
#         return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
#     else:
#         return "Привет, {name}!".format(name=name)
#
#
# @counter
# def greeting2(name: str) -> None:
#     """
#     Приветствие с именем. Вывод в консоль.
#     :param name: Имя человека.
#     :return: None.
#     """
#     print(f'Привет, {name}!')
#
#
# def main() -> None:
#     """
#     Основная функция для запуска.
#     :return: None.
#     """
#     greeting("Том")  # Вызов функции greeting с одним аргументом.
#     greeting("Миша", age=100)  # Вызов функции greeting с двумя
#     аргументами.
#     greeting2("Маша")  # Вызов функции greeting2.
#     greeting(name="Катя", age=16)  # Вызов функции greeting с именем и
#     возрастом.
#     main()  # Запуск основной функции.


# Задача 4. Кэширование для ускорения вычислений
# Создайте декоратор, который кэширует (сохраняет для дальнейшего использования)
# результаты вызова функции и, при повторном вызове с теми же аргументами,
# возвращает сохранённый результат.
# Примените его к рекурсивной функции вычисления чисел Фибоначчи.
# В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и,
# если такие аргументы уже использовались, должен вернуть сохранённый результат
# вместо запуска расчёта.

# def cache_decorator(func):
#     """
#     Декоратор для кэширования результатов функции.
#     :param func: Декорируемая функция
#     :return: Функция-обертка с кэшированием
#     """
#     cache = {} # Словарь для хранения кэшированных результатов
#     def wrapper(number):
#         """
#         Функция-обертка, которая сначала проверяет кэш перед вызовом
#         функции.
#         :param number: Аргумент для декорируемой функции
#         :return: Результат выполнения функции
#         """
#         if number in cache:
#             return cache[number] # Возвращаем результат из кэша, если он есть
#         result = func(number)
#         cache[number] = result # Сохраняем результат в кэше
#         return result
#     return wrapper
#
# @cache_decorator
# def fibonacci(number):
#     """
#     Функция для вычисления чисел Фибоначчи с использованием
#     рекурсии.
#     :param number: Позиция числа Фибоначчи
#     :return: Число Фибоначчи
#     """
#     if number <= 1:
#         return number
#     return fibonacci(number - 1) + fibonacci(number - 2)
#
# # Проверка работы декоратора и функции
# print(fibonacci(10)) # Ожидаем, что результат будет вычислен и закэширован
# print(fibonacci(10)) # Ожидаем, что результат будет возвращен из кэша
# print(fibonacci(5)) # Ожидаем, что результат будет вычислен и закэширован