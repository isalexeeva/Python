'''
n = 5
b = 5.25
f = "Hallo"
print(f"{n} - {b} - {f}")
# print("{} - {} - {}".format(n,b,f))

print("Введите первое число: ")
a = int(input())
b = int(input("Введите второе число: "))
print(f"{a} + {b} = {a+b}")

# Арифметические операции по приоритету
# 1. ** - возведение в степень
# 2. * - умножение
# 3. / - деление
# 4. // - целочисленное деление
# 5. % - остаток от деления
# 6. + - сложение
# 7. - - вычитание


# Округление

a = 5.6598
b = 3.3256
print(round(a*b, 4))

# Cокращенное присваивание
i = 2
i += 3 # i = i + 3
i -= 4 # i = i -4
# ...

# Логические операции
# >=
# <=
# == равно
# != не равно

a = 1<4 and 5>2
print(a)
a = ";"
b = "/"
print(a==b)
'''

'''
a= int(input("Введите число: "))
if a >5:
    print(a)
elif a == 5:
    print("a=5")
else:
    print("a<5")    
'''

n = 15423
sum = 0
while n>0:
    x = n % 10
    sum += x
    n = n//10
print(sum)


i = 0
while i < 5:
    # if i == 4:
    #     break
    i = i +1
else:
    print("Stop!")
print(i)