# Задача №2. Решение в группах
# Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

q = int(input())
list1 = list()
for i in range(q):
    x = int(input())
    list1.append(x)

max = max(list1)
min = min(list1)

for i in range(len(list1)):
    if list1[i] == max:
        list1[i] = min

print(list1)