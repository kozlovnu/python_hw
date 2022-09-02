# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

number = int(input("Enter your number from 1 to 7: "))
if (1 <= number <= 5):
    print("no")
elif (number == 6 or number == 7):
    print("yes")
else:
    print("The wrong number")