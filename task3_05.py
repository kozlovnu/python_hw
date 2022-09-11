# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# Fn = Fn–2 + Fn–1, где F0=0, F1=1

k = int(input('enter number k: '))
list = []
list2 = []
list.append(0)
list.append(1)
list2.append(0)
list2.append(1)

temp = 0
for i in range(2,k+1):
    temp = list[i-1]+list[i-2]
    list.append(temp)
    temp = -list2[i-1]+list2[i-2]
    list2.append(temp)
list2.reverse()
list2 = list2[:-1]

list = list2 + list
print(list)
