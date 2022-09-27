# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
string = list('aaaabbbcc')
print(string)

count = 1

for i in range(len(string)-1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            count += 1
        else:
            a = string[i]
            print(count, string[i])
            count = 1
print(count, string[i])