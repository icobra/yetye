#!/usr/bin/python3

"""
Yet Yahtzee
Sorry some txt on Ru only
"""

from random import randint
from getch import getch

print("Yet Yahtzee version 0.75")

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

def check_it(check_number):
    check_dict = {"1": 'ones',"2": 'twos',"3": 'threes',
                 "4":'fours',"5": 'fives',"6": 'sixes'}
    key_word = check_dict[str(check_number)]
    position = int(gamestat_dict['semaphore'])             
    if gamestat_dict[key_word][position] != None:
        print("Sorry, but this field is not empty.")
        return
    y = 0    
    for x in gamestat_dict['dice_list']:
        if x == check_number:
            y += 1
    if y >= 3:
        gamestat_dict[key_word][position] = 3 * check_number
    else:
        gamestat_dict[key_word][position] = 0
    next_player()

def three_of_kind():
    new_list = gamestat_dict['dice_list']
    position = int(gamestat_dict['semaphore'])
    if gamestat_dict['three_kind'][position] != None:
        print("Sorry, but this field is not empty.")
        return
    y = 0
    for x in range(1,7):
        if new_list.count(x) >= 3:
            y = x
            break       
    if y > 0:
        gamestat_dict['three_kind'][position] = sum(new_list)
    else:
        gamestat_dict['three_kind'][position] = 0    
    next_player()

def four_of_kind():
    new_list = gamestat_dict['dice_list']
    position = int(gamestat_dict['semaphore'])
    if gamestat_dict['four_kind'][position] != None:
        print("Sorry, but this field is not empty.")
        return
    y = 0
    for x in range(1,7):
        if new_list.count(x) >= 4:
            y = x
            break
    if y > 0:
        gamestat_dict['four_kind'][position] = sum(new_list)
    else:
        gamestat_dict['four_kind'][position] = 0    
    next_player()

def full_hous():
    new_list = gamestat_dict['dice_list']
    position = int(gamestat_dict['semaphore'])
    if gamestat_dict['full_hous'][position] != None:
        print("Sorry, but this field is not empty.")
        return
    y = 0
    z = 0
    k = 0
    for x in range(1,7):
        if new_list.count(x) == 3:
            y = x
        if new_list.count(x) == 2:
            z = x
        if new_list.count(x) == 5:
            k = 5           
    if y > 0 and z > 0:
        gamestat_dict['full_hous'][position] = 25
    elif k == 5:
        gamestat_dict['full_hous'][position] = 25       
    else:
        gamestat_dict['full_hous'][position] = 0    
    next_player()

def small_straight():
    position = int(gamestat_dict['semaphore'])
    new_list = gamestat_dict['dice_list']
    new_list = sorted(new_list)
    new_list.pop()
    y = new_list[0]
    new_list.pop(0)
    for x in new_list:
        if x == y + 1:
            y += 1
        else:
            y = 0
            break
    if y > 0:
        gamestat_dict['sstraight'][position] = 30
    else:
        new_list = gamestat_dict['dice_list']
        new_list = sorted(new_list)
        new_list.pop(0)
        y = new_list[0]
        new_list.pop(0)
        for x in new_list:
            if x == y +1:
                y += 1
            else:
                y = 0
                break
        if y > 0:
            gamestat_dict['sstraight'][position] = 30
        else:    
            gamestat_dict['sstraight'][position] = 0
    next_player()                         

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
    next_player()

def chance():
    position = int(gamestat_dict['semaphore'])
    if gamestat_dict['chance'][position] != None:
        print("Sorry, but this field is not empty.")
        return
    y = 0    
    for x in gamestat_dict['dice_list']:
        y += x
    gamestat_dict['chance'][position] = y
    next_player()    

def quit():
    print("Thank you. Take a good day.")
    exit()

def put_aside():
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

def roll_dice6d():
    #Game dice 6d
    number = 5 - len(gamestat_dict['dice_list'])
    try_roll = gdict['try_roll']
    print("Roll the dices...")
    new_list = []
    for i in range(0, number):
        dice_number = randint(1,6)
        new_list.append(dice_number)
    print(new_list)
    try_roll += 1
    gamestat_dict['try_roll'] = try_roll
    gamestat_dict['dice_list'] = gamestat_dict['dice_list'] + new_list
    print(gamestat_dict['dice_list'])
    print(try_roll)

def next_player():
    gamestat_dict['try_roll'] = 0
    gamestat_dict['dice_list'] = []    
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
        choice()
        board()
    else:
        print("Enter avalibal command")