# Задание 1: Язык математики
# В первый же день на сайте отвалилась формула по расчёту рекламной метрики, и только Вася может её поправить. Часть программы с вводными данными представлена ниже, отдельно записана формула на математическом языке.
# Дана программа:
# a=8
# b = 10
# c = 12
# d = 18
# Продолжите программу: переведите выражение с математического языка на язык Python, запишите его в переменную res и выведите результат.

a = 8
b = 10
c = 12
d = 18

chisl = (-3 + a ** 2)*b-2** 3
znam = c - 2 * d
rez = chisl / znam

print(chisl, znam)
print(rez)
