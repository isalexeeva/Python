# Задание 2. Сумма чисел
# В файле zen.txt хранится так называемый Дзен Пайтона — текст философии
# программирования на языке Python. Выглядит он так:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# Напишите программу, которая выводит на экран все строки этого файла в
# обратном порядке.
# Кстати, попробуйте открыть консоль Python и ввести команду import this.
# Результат работы программы:
# Namespaces are one honking great idea -- let's do more of those!
# If the implementation is easy to explain, it may be a good idea.
# If the implementation is hard to explain, it's a bad idea.
# Although never is often better than *right* now.
# …
# Подсказка № 1
# Перед открытием файла убедитесь, что он существует в ожидаемом месте. Если файл
# не существует или имеет другое имя, программа не сможет его открыть. Проверьте
# путь к файлу и его наличие.
# Подсказка № 2
# Откройте файл для чтения с помощью функции open(). Убедитесь, что файл открыт в
# режиме чтения ("r"). Используйте метод readlines() для получения всех строк
# файла в виде списка.
# Подсказка № 3
# Закройте файл после чтения данных, чтобы освободить ресурсы и избежать утечек
# памяти. Используйте метод close() для закрытия файла.
# Подсказка № 4
# Используйте функцию reversed() для переворачивания списка строк. Обратите
# внимание, что reversed() возвращает итератор, который нужно итерировать для
# получения перевернутого списка.

# Открываем файл zen.txt для чтения
with open('zen.txt', 'r') as file:
    # Считываем все строки файла в список
    lines = file.readlines()

# Переворачиваем список строк с помощью функции reversed()
reversed_lines = reversed(lines)

# Выводим строки в обратном порядке
for line in reversed_lines:
    print(line.strip())  # Убираем лишние символы перевода строки