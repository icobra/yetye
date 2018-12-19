#!/usr/bin/python3

"""
Yet Yahtzee ver 0.0012

Sorry some txt on Ru only

"""
from random import randint
from getch import getch

print("Yet Yahtzee version 0.0012")

# Important variable
gamestat_dict = {
    'semaphore': 0,
    'try_roll': 0,
    'dice_list':[],
    'ones': None,
    'twos': None, 
    'threes': None,
    'fours': None,
    'fives': None,
    'sixes': None,
    'bonus': None,
    'three_kind': None,
    'four_kind': None,
    'full_hous': None,
    'sstraight': None,
    'lstraight': None,
    'yacht': None,
    'chance': None,
    'total': None
}

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

def board():
    # Main screen
    print("name                   Player1         Player2")
    print("(1)Ones                  %s" % gamestat_dict['ones'])
    print("(2)Twos                  %s" % gamestat_dict['twos'])
    print("(3)Threes                %s" % gamestat_dict['threes'])
    print("(4)Fours                 %s" % gamestat_dict['fours'])
    print("(5)Fives                 %s" % gamestat_dict['fives'])
    print("(6)Sixes                 %s" % gamestat_dict['sixes'])
    print("""Bonus

(T)Three of a kind
(F)Four of a kind
(H)Full Hous
(S)Small Straight
(L)Large Straight
(Y)Yahtzee
(C)Chance

Total:""")
    print("(W)Watch game rules (Q)Quit (P)Put aside (R)Roll the dice   Try %d/3" % gamestat_dict['try_roll'])
    print("Current dice: {}".format (gamestat_dict['dice_list']))
#    print(gamestat_dict['dice_list']) 

def check_it(gdict = gamestat_dict):
    if gdict['ones'] != None:
        print("Sorry, but this field is not empty.")
        return
    y = 0    
    for x in gdict['dice_list']:
        if x == 1:
            y += 1
    if y >= 3:
        gdict['ones'] = 3
    else:
        gdict['ones'] = 0
    gdict['try_roll'] = 0
    gdict['dice_list'] = []

def check_it2(gdict = gamestat_dict):
    if gdict['twos'] != None:
        print("Sorry, but this field is not empty.")
        return
    y = 0    
    for x in gdict['dice_list']:
        if x == 2:
            y += 2
    if y >= 6:
        gdict['twos'] = 6
    else:
        gdict['twos'] = 0
    gdict['try_roll'] = 0
    gdict['dice_list'] = []

def check_it3(gdict = gamestat_dict):
    if gdict['threes'] != None:
        print("Sorry, but this field is not empty.")
        return
    y = 0    
    for x in gdict['dice_list']:
        if x == 3:
            y += 3
    if y >= 9:
        gdict['threes'] = 9
    else:
        gdict['threes'] = 0
    gdict['try_roll'] = 0
    gdict['dice_list'] = []

def check_it4(gdict = gamestat_dict):
    if gdict['fours'] != None:
        print("Sorry, but this field is not empty.")
        return
    y = 0    
    for x in gdict['dice_list']:
        if x == 4:
            y += 4
    if y >= 12:
        gdict['fours'] = 4
    else:
        gdict['fours'] = 12
    gdict['try_roll'] = 0
    gdict['dice_list'] = []

def check_it5(gdict = gamestat_dict):
    if gdict['fives'] != None:
        print("Sorry, but this field is not empty.")
        return
    y = 0    
    for x in gdict['dice_list']:
        if x == 5:
            y += 5
    if y >= 15:
        gdict['fives'] = 15
    else:
        gdict['fives'] = 0
    gdict['try_roll'] = 0
    gdict['dice_list'] = []

def check_it6(gdict = gamestat_dict):
    if gdict['sixes'] != None:
        print("Sorry, but this field is not empty.")
        return
    y = 0    
    for x in gdict['dice_list']:
        if x == 6:
            y += 18
    if y >= 18:
        gdict['sixes'] = 18
    else:
        gdict['sixes'] = 0
    gdict['try_roll'] = 0
    gdict['dice_list'] = []

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

def chance(gdict = gamestat_dict):
    if gdict['chance'] != None:
        print("Sorry, but this field is not empty.")
        return
    y = 0    
    for x in gdict['dice_list']:
        y += x
    gdict['chance'] = y

def quit():
    print("Thank you. Take a good day.")
    exit()

def put_aside(gdict = gamestat_dict):
    #Put aside some dice if possible
    hold_dice = gamestat_dict['dice_list']
    x = len(hold_dice)
    if x > 0:
        print("\nYou can put aside some dice.\n")
        print("Current dices:    {}".format (hold_dice))
        x += 1
        number_list = list(range(1, x))
        print("Number of dices:  {}".format (number_list))
        print("Enter the numbers of the dices through the space to remove them.")
        user_choice = (input("Enter the space - hold all dices....")).strip()
        user_choice = user_choice.split(" ")
        print(user_choice)
        user_choice = sorted(user_choice)
        print(user_choice)
        y = len(user_choice)
        if y > x or y == 0:
            print("You can't remove more dices than you have.")
        while y > 0:
            hold_dice.pop((int(user_choice.pop()))-1)
            y -= 1
        print(hold_dice)
    else:
        print("You can't hold something.")    

def roll_dice6d(gdict = gamestat_dict):
    #Game dice 6d
    number = 5 - len(gdict['dice_list'])
    try_roll = gdict['try_roll']
    print("Roll the dices...")
    new_list = []
    for i in range(0, number):
        dice_number = randint(1,6)
        new_list.append(dice_number)
    print(new_list)
    try_roll += 1
    gdict['try_roll'] = try_roll
    gdict['dice_list'] = gdict['dice_list'] + new_list
    print(gdict['dice_list'])
    print(try_roll)

action_dict = {'1': check_it,
                '2': check_it2,
                '3': check_it3,
                '4': check_it4,
                '5': check_it5,
                '6': check_it6,
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
                'R': roll_dice6d
}

board()
while True:
    print("Make you choice...")
    choice = getch().upper()
    if choice == 'R' or choice == 'P': 
        if gamestat_dict['try_roll'] == 3:
            board()
            print("Make choice. No more dice rolls this turn.")            
        else:
            print(choice)
            choice = action_dict[choice]
            # board()
            choice()
            board()
    elif choice in action_dict.keys():
        print(choice)
        choice = action_dict[choice]
        board()
        choice()
        board()
    else:
        print("Enter avalibal command")