# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import random

n = int(input("Enter number: "))
numbers = []
for i in range(n):
    numbers.append(random.randint(-n,n))
print(numbers)
with open('numbers.txt','w') as data:
    for j in range(len(numbers)):
        data.write(f'{numbers[j]}\n')

path = 'numbers.txt'
data = open(path, 'r')
mult = 1
for line in data:
    if int(line) != 0:
        mult*=int(line)
data.close()
print(mult)