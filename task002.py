# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

x = int(input("enter X: "))
y = int(input("enter Y: "))
z = int(input("enter z: "))

left = not(x or y or z)
right = not x and not y and not z
result = left == right
print(result)
