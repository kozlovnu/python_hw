# нахождения среднего арифметического из 4-х чисел
a = [1, 2, 3, 4]
sum = 0

for i in a:
    sum += i

print(sum/len(a))


# нахождения факториала N
f = 3
n = 1

for i in range(1, f+1):
    n *= i

print(n)