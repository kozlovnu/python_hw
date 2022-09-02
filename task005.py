# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
import math
x1 = int(input("enter coordinate x1: "))
y1 = int(input("enter coordinate y1: "))
x2 = int(input("enter coordinate x2: "))
y2 = int(input("enter coordinate y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("{0:.3f}".format(distance))