# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

some_list = list(input('Enter expression: '))
print(some_list)
digits = []
signs = []
def FindDigits(some_list):
    for i in some_list:
        if i.isdigit():
            digits.append(i)
        else:
            signs.append(i)
    return digits, signs


def FindSigns(some_list, signs):
    for i in range(some_list):
        if some_list[i] == '+':
            signs = int(some_list[i-1])+int(some_list[i+1])
    return signs

def Expression(Function()):
    for i in list_2:
        if i == '+':
            result = list[0]+list[1]
        elif i == '-':
            result = list[0] - list[1]
        elif i == '*':
            result = list[0] * list[1]
        elif i == '/':
            result = list[0] / list[1]
    return result

print(*FindDigits(some_list))
print(Expression(FindDigits(some_list)))
# print(FindSigns(some_list,signs))