# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).

x = int(input("enter coordinate x: "))
y = int(input("enter coordinate y: "))

if (x != 0 and y != 0):
    if (x > 0 and y > 0):
        print("the point is in the first plane")
    elif (x < 0 and y > 0):
        print("the point is in the second plane")
    elif (x < 0 and y < 0):
        print("the point is in the third plane")
    elif (x > 0 and y < 0):
        print("the point is in the fourth plane")
else:
    print("x & y must be different from 0")
