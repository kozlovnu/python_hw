# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

some_string = input('enter expression: ')

def subdivide_by_brackets(some_string):
    if "(" in some_string:
        some_string = some_string.replace(some_string[some_string.index('('):],
                                          subdivide_by_brackets(some_string[some_string.index('(') + 1:]))
    if ")" in some_string:
        some_string = some_string.replace(some_string[0:some_string.index(')') + 1],
                                          str(split_into_arfim(some_string[0:some_string.index(')')])))
        return some_string
    return split_into_arfim(some_string)


def split_into_arfim(some_sting, list_of_operators=['-', '+', '*', '/']):
    operator = []
    numbers = []
    temp = ''
    for char in some_sting:
        if not char in list_of_operators:
            temp += char
        else:
            operator.append(char)
            try:
                numbers.append(float(temp))
            except:
                print('stupid symbol')
                exit()
            temp = ''
    numbers.append(float(temp))
    while len(numbers) > 1:
        if '*' in operator:
            index = operator.index('*')
            temp = parser(numbers[index], numbers[index + 1], '*')
            numbers[index] = temp
        elif '/' in operator:
            index = operator.index('/')
            temp = parser(numbers[index], numbers[index + 1], '/')
            numbers[index] = temp
        elif '+' in operator:
            index = operator.index('+')
            temp = parser(numbers[index], numbers[index + 1], '+')
            numbers[index] = temp
        elif '-' in operator:
            index = operator.index('-')
            temp = parser(numbers[index], numbers[index + 1], '-')
            numbers[index] = temp
        del (numbers[index + 1])
        del (operator[index])
    return numbers[0]


def parser(num1, num2, operator):
    try:
        if operator == '+':
            return num1 + num2
        if operator == '-':
            return num1 - num2
        if operator == '*':
            return num1 * num2
        if operator == '/':
            try:
                return num1 / num2
            except:
                print('Division by zero')
                exit()
    except:
        print('Unexpected vlaues')
        exit()

# print(some_string)
print(f'Result of {some_string} is',subdivide_by_brackets(some_string))
