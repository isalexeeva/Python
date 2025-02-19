# Задача 3. Палиндром
# Используя модуль collections, реализуйте функцию can_be_poly, которая
# принимает на вход строку и проверяет, можно ли получить из неё палиндром.
# Пример кода:
# print(can_be_poly('abcba'))
# print(can_be_poly('abbbc'))
# Результат:
# True
# False

from collections import Counter

def can_be_poly(s: str) -> bool:
    # Считаем количество вхождений каждого символа
    char_count = Counter(s)
    # Подсчитываем количество символов с нечётным количеством вхождений
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    # Палиндром возможен, если таких символов не больше одного
    return odd_count <= 1
