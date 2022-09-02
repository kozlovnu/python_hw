# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных
# координат точек в этой четверти (x и y).

plane = int(input("enter the number of the plane: "))
if (1 < plane and plane > 4):
    print(f"there is no plane with number {plane}")
else:
    if (plane == 1):
        print("x > 0, y > 0")
    elif (plane == 2):
        print("x < 0, y > 0")
    elif (plane == 3):
        print("x < 0, y < 0")
    elif (plane == 4):
        print("x > 0, y < 0")
