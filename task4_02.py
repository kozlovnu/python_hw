# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

a = int(input('n '))
numbers = []
i = 2
while i < a:
    if a % i == 0:
        numbers.append(i)
        a /= i
    else:
        i += 1
numbers.append(int(a))
print(numbers)