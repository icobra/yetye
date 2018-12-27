#!/usr/bin/python3

"""
Yet Yahtzee
Sorry some txt on Ru only
"""

from random import randint
from getch import getch

print("Yet Yahtzee version 0.5")

# Important variable
gamestat_dict = {
    'semaphore': 0,
    'try_roll': 0,
    'dice_list':[],
    'ones': [None, None],
    'twos': [None, None],
    'threes': [None, None],
    'fours': [None, None],
    'fives': [None, None],
    'sixes': [None, None],
    'bonus': [None, None],
    'three_kind': [None, None],
    'four_kind': [None, None],
    'full_hous': [None, None],
    'sstraight': [None, None],
    'lstraight': [None, None],
    'yacht': [None, None],
    'chance': [None, None],
    'total': [None, None],
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
    if gamestat_dict['semaphore'] == 0:
        print("name                   *Player1         Player2")
    else:
        print("name                   Player1         *Player2")
    print("(1)Ones                  %s            %s" % (gamestat_dict['ones'][0], gamestat_dict['ones'][1]))
    print("(2)Twos                  %s            %s" % (gamestat_dict['twos'][0], gamestat_dict['twos'][1]))
    print("(3)Threes                %s            %s" % (gamestat_dict['threes'][0], gamestat_dict['threes'][1]))
    print("(4)Fours                 %s            %s" % (gamestat_dict['fours'][0], gamestat_dict['fours'][1]))
    print("(5)Fives                 %s            %s" % (gamestat_dict['fives'][0], gamestat_dict['fives'][1]))
    print("(6)Sixes                 %s            %s" % (gamestat_dict['sixes'][0], gamestat_dict['sixes'][1]))
    print("   Bonus                 %s            %s" % (gamestat_dict['bonus'][0], gamestat_dict['bonus'][1]))
    print("")
    print("(T)Three of a kind       %s            %s" % (gamestat_dict['three_kind'][0], gamestat_dict['three_kind'][1]))
    print("(F)Four of a kind        %s            %s" % (gamestat_dict['four_kind'][0], gamestat_dict['four_kind'][1]))
    print("(H)Full Hous             %s            %s" % (gamestat_dict['full_hous'][0], gamestat_dict['full_hous'][1]))
    print("(S)Small Straight        %s            %s" % (gamestat_dict['sstraight'][0], gamestat_dict['sstraight'][1]))
    print("(L)Large Straight        %s            %s" % (gamestat_dict['lstraight'][0], gamestat_dict['lstraight'][1]))
    print("(Y)Yahtzee               %s            %s" % (gamestat_dict['yacht'][0], gamestat_dict['yacht'][1]))
    print("(C)Chance                %s            %s" % (gamestat_dict['chance'][0], gamestat_dict['chance'][1]))
    print("")
    print("Total: ")
    print("(W)Watch game rules (Q)Quit (P)Put aside (R)Roll the dice   Try %d/3" % gamestat_dict['try_roll'])
    print("Current dice: {}".format (gamestat_dict['dice_list']))

def check_it(check_number, gdict = gamestat_dict):
    print(check_number)
    check_dict = {"1": 'ones',"2": 'twos',"3": 'threes',
                 "4":'fours',"5": 'fives',"6": 'sixes'}
    key_word = check_dict[str(check_number)]
    position = int(gamestat_dict['semaphore'])             
    if gdict[key_word][position] != None:
        print("Sorry, but this field is not empty.")
        return
    y = 0    
    for x in gdict['dice_list']:
        if x == check_number:
            y += 1
    if y >= 3:
        gdict[key_word][position] = 3 * check_number
    else:
        gdict[key_word][position] = 0
    gdict['try_roll'] = 0
    gdict['dice_list'] = []
    next_player()

def three_of_kind():
    new_list = gamestat_dict['dice_list']
    position = int(gamestat_dict['semaphore'])
    print("Тут")
    if gamestat_dict['three_kind'][position] != None:
        print("Sorry, but this field is not empty.")
        print("цикл")
        return
    y = 0
    print("поехали")    
    for x in range(1,7):
        if new_list.count(x) >= 3:
            y = x
            print("хм")
            break
    print(y)            
    if y > 0:
        print("Может здесь")
        gamestat_dict['three_kind'][position] = sum(new_list)
        print(sum(new_list))
        print("Сумма")
    else:
        gamestat_dict['three_kind'][position] = 0    
    gamestat_dict['try_roll'] = 0
    gamestat_dict['dice_list'] = []
    next_player()

def four_of_kind():
    pass

def full_hous():
    pass

def small_straight():
    pass

def large_straight():
    pass

def yahtzee():
    position = int(gamestat_dict['semaphore'])
    check_number = gamestat_dict['dice_list'][0]             
    if gamestat_dict['yacht'][position] != None:
        print("Sorry, but this field is not empty.")
        return
    y = 0    
    for x in gamestat_dict['dice_list']:
        if x == check_number:
            y += 1
    if y == 5:
        gamestat_dict['yacht'][position] = 50
    else:
        gamestat_dict['yacht'][position] = 0
    gamestat_dict['try_roll'] = 0
    gamestat_dict['dice_list'] = []
    next_player()

def chance(gdict = gamestat_dict):
    position = int(gamestat_dict['semaphore'])
    if gdict['chance'][position] != None:
        print("Sorry, but this field is not empty.")
        return
    y = 0    
    for x in gdict['dice_list']:
        y += x
    gdict['chance'][position] = y
    gamestat_dict['try_roll'] = 0
    gamestat_dict['dice_list'] = []
    next_player()    

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

def next_player():
    if gamestat_dict['semaphore'] == 0:
        gamestat_dict['semaphore'] = 1
    else:
        gamestat_dict['semaphore'] = 0

def total():
    pass

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
                'R': roll_dice6d
}

board()
while True:
    if gamestat_dict['semaphore'] == 0:
        print("Player1, Make you choice...")
    else:
        print("Player2, Make you choice...")
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
    elif choice in ['1', '2', '3', '4', '5', '6']:
        check_number = int(choice)
        choice = action_dict[choice]
        choice(check_number)
        board()
    elif choice in action_dict.keys():
        print(choice)
        choice = action_dict[choice]
        board()
        choice()
        board()
    else:
        print("Enter avalibal command")