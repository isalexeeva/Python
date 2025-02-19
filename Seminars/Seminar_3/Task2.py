# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list = [1, 2, 3, 4, 5]
list_res = []
k = int(input("Введите целое положительное число: "))
k = k % len(list)
for i in range(k):
    list_res.append(list[len(list)  -1 -i])
print(list_res) 

for i in range(len(list) - k):
    list_res.append(list[i])

print(list_res)    
