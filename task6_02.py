# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

numbers = [1, 2, 3, 5, 1, 5, 3, 10]
new_numbers = []
count = 0
for i in range(len(numbers)):
    if numbers[i] not in numbers[i+1:] and numbers[i] not in numbers[:i-1:]:
        new_numbers.append(numbers[i])
print(new_numbers)