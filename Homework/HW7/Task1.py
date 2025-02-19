# Задание 1. Новые списки
# Даны три списка:
# 1. floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# 2. names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# 3. numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
# Напишите код, который создаёт три новых списка. Вот их содержимое:
# 1. Каждое число из списка floats возводится в третью степень и округляется
# до трёх знаков после запятой.
# 2. Из списка names берутся только имена минимум из пяти букв.
# 3. Из списка numbers берётся произведение всех чисел.

from typing import List
from functools import reduce

# Исходные списки
floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

# 1. Возведение чисел из floats в третью степень и округление до трёх знаков после запятой
floats_cubed_rounded: List[float] = list(map(lambda x: round(x**3, 3), floats))

# 2. Фильтрация имён из names, оставляем только имена минимум из пяти букв
long_names: List[str] = list(filter(lambda name: len(name) >= 5, names))

# 3. Вычисление произведения всех чисел из numbers
numbers_product: int = reduce(lambda x, y: x * y, numbers)

# Вывод результатов
print("1. Числа из floats, возведённые в третью степень и округлённые:", floats_cubed_rounded)
print("2. Имена из names, состоящие минимум из пяти букв:", long_names)
print("3. Произведение всех чисел из numbers:", numbers_product)