# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import numpy as np

koef = np.random.randint(0,101, int(input('enter k ')))
poly = np.poly1d(koef, variable = 'x')
print(poly)