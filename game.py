#!/usr/bin/python3

"""
Yet Yahtzee ver 0.003

Sorry some txt on Ru only

"""
from random import randint


print("Yet Yahtzee")

def Rules():
    print("""
                   Правила игры в Yahtzee.

Игра длиться 13 раундов

В течении раунда делается три броска

Перебросить не более двух раз можно от 0 до 5 кубиков

По окончанию раунда нужно выбрать одну из 13 ячеек для внесения результата.


                   Начисление очков в ячейкии.
Верхнее поле:

Ones - единицы, если три, то результат 3 очка, иначе ноль

Twos - двойки, если три, то результат 6 очков, иначе ноль

Threes - тройки, если три, то результат 9 очков, иначе ноль

Fours - четверки, если четыре, то результат 12 очков, иначе ноль

Fives - пятерки, если три, то результат 15 очков, иначе ноль

Sixes - шестерки, если три, то результат 18 очков, иначе ноль

Bonus - начисляется, если в нижнем поле больше 63 очков, иначе ноль

Нижнее поле:
(При несоблюдении условий записывается 0)

Three of a Kind - сумма трех одинаковых плюс сумма остальных кубиков

Four of a Kind - сумма четырех одинаковых плюс сумма остальных кубиков

Full Hous - 25 очков, три одинаковых плюс два одинаковых кубика

Small Straight - 30 очков, выпадает 1-2-3-4, 2-3-4-5 или 3-4-5-6

Large Straight - 40 очков, выпадает 1-2-3-4-5 или 2-3-4-5-6

Yahtzee - 50 очков, 5 одинаковых кубиков

Chance - сумма выпавших кубиков, любая комбинация.

        """)

def Board():
    print("""
name                   Player1         Player2

(1)Ones 
(2)Twos 
(3)Threes
(4)Fours
(5)Fives
(6)Sixes
Bonus

(T)Three of a kind
(F)Four of a kind
(H)Full Hous
(S)Small Straight
(L)Large Straight
(Y)Yahtzee
(C)Chance

Total:

(W)Watch game rules (Q)Quit (P)Put aside (R)Roll the dice""")


def dice6d(self):
    #Игровой кубик с 6-ю гранями
    print("Бросим кости")
    dice_number = randint(1,6)
    return dice_number


choice = Board


x = True
while x:
    choice()
    break

