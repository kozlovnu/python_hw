# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input("enter your number: "))
calc = ""
while n > 0:
    x = str(n % 2)
    calc = x + calc
    n = int(n / 2)
print(calc)
