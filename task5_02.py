# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random

#take = candy-candy//28*28

candy = 221
player1 = 1
player2 = 2
player = random.randint(1,3)
print('Candy left: ', candy)
while candy>0:
    if player == 1:
        print("1st player turn")
        take = candy-candy//29*29
        if take == 0:
            take = 1
        print(f'1st player takes {take} candys')
        candy = candy-take
        print("Candy left: ",candy)
        if candy == 0:
            print('The 1st player win!')
        else:
            player = 2
    else:
        print("2nd player turn")
        take = int(input('Enter numbers of candys to take from 1 to 28: '))
        candy = candy-take
        print("Candy left: ", candy)
        if candy == 0:
            print('The 2nd player win!')
        else:
            player = 1