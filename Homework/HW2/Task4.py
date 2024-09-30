# Задача 4. Посчитай чужую зарплату...
# Бухгалтер устала постоянно считать вручную среднегодовую зарплату
# сотрудников компании и, чтобы облегчить себе жизнь, обратилась к
# программисту.
# Напишите программу, которая принимает от пользователя зарплату сотрудника
# за каждый из 12 месяцев и выводит на экран среднюю зарплату за год.

sum_salary = 0
months = 12
for month in range(1, months+1):
    print(f"Зарплата за {month}-й месяй: ")
    salary = float(input())
    sum_salary += salary
print(f"Среднегодовая зарплата составила {round(sum_salary/12, 2)}")

