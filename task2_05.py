# Реализуйте алгоритм перемешивания списка.
import random
n = int(input("Enter lenght of list: "))
list = []
for i in range(n):
    print(f'Enter {i+1} element:\n')
    list.append(input())
print('исходный список:', list)
random.shuffle(list)
print('перемешанный список: ',list)