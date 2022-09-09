# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list = [int(n) for n in input('enter numbers splitted by space: ').split()]
print(list)
sum=0
for i in range(len(list)):
    if i%2!=0:
        sum+=int(list[i])
print('sum is ',sum)
