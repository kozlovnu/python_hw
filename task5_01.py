# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

words = 'Это программа абва удаляющая из текста прпрабвва все слова содержащие "абв"'
print(words)
new_words = list(filter(lambda x: 'абв' not in x, words.split()))
print(*new_words)
