#!/usr/bin/python3

"""
Yet Yahtzee ver 0.007

Sorry some txt on Ru only

"""
from random import randint
from getch import getch

print("Yet Yahtzee version 0.007")

# List of avalibal action, keys to dictonary
action_list = ('1', '2', '3', '4', '5', '6', 'T', 'F', 'H', 'S',
    'L', 'Y', 'C', 'W', 'Q', 'P', 'R') 

def watch_game_rules():
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
    # Main screen
    print("""name                   Player1         Player2

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


def check_it():
    print ("a, v bbbbbbc")

def three_of_kind():
    pass

def four_of_kind():
    pass

def full_hous():
    pass

def small_straight():
    pass

def large_straight():
    pass

def yahtzee():
    pass

def chance():
    pass

def quit():
    print("Thank you. Take a good day.")
    exit()

def put_aside():
    pass


def roll_dice6d(self):
    #Game dice 6d
    print("Roll the dice...")
    dice_number = randint(1,6)
    return dice_number

action_dict = {'1': check_it,
                '2': check_it,
                '3': check_it,
                '4': check_it,
                '5': check_it,
                '6': check_it,
                'T': three_of_kind,
                'F': four_of_kind,
                'H': full_hous,
                'S': small_straight,
                'L': large_straight,
                'Y': yahtzee,
                'C': chance,
                'W': watch_game_rules,
                'Q': quit,
                'P': put_aside,
                'R': roll_dice6d}

choice = Board
choice()

while True:
    print("Make you choice...")
    choice = getch().upper()
    if choice in action_list:
        print(choice)
        plzwork = action_dict[choice]
        plzwork()
        print("Тадамсь")
    else:
        print("Enter avalibal command")