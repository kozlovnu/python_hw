# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Enter your number: "))
result = []
a=1
for i in range(n):
    if i == 0:
        result.append(1)
    else:
        a *= (i+1)
        result.append(a)
print(result)