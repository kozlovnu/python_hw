# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = float(input("enter your number: "))
sum = 0

x = str(n).split(".")
a = int(x[0])
b = int(x[1])
sum = 0
while (a != 0):
    sum += (a % 10)
    a = a // 10
while (b != 0):
    sum += (b % 10)
    b = b // 10
print(f"Sum of {n} is:", sum)
