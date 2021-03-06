#!/usr/bin/python3

"""
Yet Yahtzee - board game
Sorry some txt on Ru only
"""

import sys
from random import randint
from getch import getch

print("Yet Yahtzee version 0.97")

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
    'full_house': [None, None],
    'sstraight': [None, None],
    'lstraight': [None, None],
    'yacht': [None, None],
    'chance': [None, None],
    'total': [None, None],
}

def watch_game_rules(file_name=str("rules_ru.txt")) -> None:
    """Show game rules to user"""
    with open(file_name) as rules:
        for line in rules:
            print(line, end=' ')
    print("Нажмите любую клавишу для продолжения")
    getch()

def show_board(board: dict) -> None:
    """ Main screen,show board to user """
    if board['semaphore'] == 0:
        print("name                 *Player1     Player2")
    else:
        print("name                 Player1     *Player2")
    print("(1)Ones                %s        %s" % (board['ones'][0], board['ones'][1]))
    print("(2)Twos                %s        %s" % (board['twos'][0], board['twos'][1]))
    print("(3)Threes              %s        %s" % (board['threes'][0], board['threes'][1]))
    print("(4)Fours               %s        %s" % (board['fours'][0], board['fours'][1]))
    print("(5)Fives               %s        %s" % (board['fives'][0], board['fives'][1]))
    print("(6)Sixes               %s        %s" % (board['sixes'][0], board['sixes'][1]))
    print("   Bonus               %s        %s" % (board['bonus'][0], board['bonus'][1]))
    print("")
    print("(T)Three of a kind     %s        %s" % (board['three_kind'][0], board['three_kind'][1]))
    print("(F)Four of a kind      %s        %s" % (board['four_kind'][0], board['four_kind'][1]))
    print("(H)Full House          %s        %s" % (board['full_house'][0], board['full_house'][1]))
    print("(S)Small Straight      %s        %s" % (board['sstraight'][0], board['sstraight'][1]))
    print("(L)Large Straight      %s        %s" % (board['lstraight'][0], board['lstraight'][1]))
    print("(Y)Yahtzee             %s        %s" % (board['yacht'][0], board['yacht'][1]))
    print("(C)Chance              %s        %s" % (board['chance'][0], board['chance'][1]))
    print("")
    print("Total:                 %s        %s" % (board['total'][0], board['total'][1]))
    print("(W)Watch game rules (Q)Quit (P)Put aside (R)Roll the dice  Try %d/3" % board['try_roll'])
    print("Current dice: {}".format(board['dice_list']))

def check_top_field(dice_number: int) -> None:
    """Check top field condition"""
    check_dict = {"1":'ones', "2":'twos', "3": 'threes',
                  "4":'fours', "5":'fives', "6": 'sixes'}
    key_word = check_dict[str(dice_number)]
    position = int(gamestat_dict['semaphore'])
    if gamestat_dict[key_word][position] is not None:
        print("Sorry, but this field is not empty.")
        return
    dice_repeats = 0
    for dice in gamestat_dict['dice_list']:
        if dice == dice_number:
            dice_repeats += 1
    if dice_repeats >= 3:
        gamestat_dict[key_word][position] = 3 * dice_number
    else:
        gamestat_dict[key_word][position] = 0
    next_player()

def three_of_kind() -> None:
    """Check three of kind condition"""
    new_list = gamestat_dict['dice_list']
    position = int(gamestat_dict['semaphore'])
    if gamestat_dict['three_kind'][position] is not None:
        print("Sorry, but this field is not empty.")
        return
    dice_repeats = 0
    for dice_number in range(1, 7):
        if new_list.count(dice_number) >= 3:
            dice_repeats = dice_number
            break
    if dice_repeats > 0:
        gamestat_dict['three_kind'][position] = sum(new_list)
    else:
        gamestat_dict['three_kind'][position] = 0
    next_player()

def four_of_kind() -> None:
    """Check three of kind condition"""
    new_list = gamestat_dict['dice_list']
    position = int(gamestat_dict['semaphore'])
    if gamestat_dict['four_kind'][position] is not None:
        print("Sorry, but this field is not empty.")
        return
    dice_repeats = 0
    for dice_number in range(1, 7):
        if new_list.count(dice_number) >= 4:
            dice_repeats = dice_number
            break
    if dice_repeats > 0:
        gamestat_dict['four_kind'][position] = sum(new_list)
    else:
        gamestat_dict['four_kind'][position] = 0
    next_player()

def full_house() -> None:
    """Check full house condition"""
    new_list = gamestat_dict['dice_list']
    position = int(gamestat_dict['semaphore'])
    if gamestat_dict['full_house'][position] is not None:
        print("Sorry, but this field is not empty.")
        return
    three_dice = False
    two_dice = False
    five_dice = False
    for dice_number in range(1, 7):
        if new_list.count(dice_number) == 3:
            three_dice = True
        if new_list.count(dice_number) == 2:
            two_dice = True
        if new_list.count(dice_number) == 5:
            five_dice = True
    if three_dice and two_dice:
        gamestat_dict['full_house'][position] = 25
    elif five_dice:
        gamestat_dict['full_house'][position] = 25
    else:
        gamestat_dict['full_house'][position] = 0
    next_player()

def check_small_straight() -> None:
    """Check small_straight condition"""
    position = int(gamestat_dict['semaphore'])
    if gamestat_dict['sstraight'][position] is not None:
        print("Sorry, but this field is not empty.")
        return
    small_straight = False
    new_list = gamestat_dict['dice_list']
    new_list = sorted(set(new_list))
    control_list = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    if len(new_list) == 4:
        if new_list in control_list:
            small_straight = True
    if len(new_list) == 5:
        if new_list[:-1] in control_list or new_list[1:] in control_list:
            small_straight = True
    if small_straight:
        gamestat_dict['sstraight'][position] = 30
    else:
        gamestat_dict['sstraight'][position] = 0
    next_player()

def check_large_straight() -> None:
    """Check large_straight condition"""
    position = int(gamestat_dict['semaphore'])
    if gamestat_dict['lstraight'][position] is not None:
        print("Sorry, but this field is not empty.")
        return
    large_straight = False
    new_list = gamestat_dict['dice_list']
    new_list = sorted(new_list)
    control_list = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
    if new_list in control_list:
        large_straight = True
    if large_straight:
        gamestat_dict['lstraight'][position] = 40
    else:
        gamestat_dict['lstraight'][position] = 0
    next_player()

def check_yahtzee() -> None:
    """Check yahtzee condition"""
    position = int(gamestat_dict['semaphore'])
    if gamestat_dict['yacht'][position] is not None:
        print("Sorry, but this field is not empty.")
        return
    yahtzee = False
    new_list = gamestat_dict['dice_list']
    new_list = sorted(set(new_list))
    if len(new_list) == 1:
        yahtzee = True
    if yahtzee:
        gamestat_dict['yacht'][position] = 50
    else:
        gamestat_dict['yacht'][position] = 0
    next_player()

def check_chance() -> None:
    """Check chance condition"""
    position = int(gamestat_dict['semaphore'])
    if gamestat_dict['chance'][position] is not None:
        print("Sorry, but this field is not empty.")
        return
    dice_sum = 0
    for dice_number in gamestat_dict['dice_list']:
        dice_sum += dice_number
    gamestat_dict['chance'][position] = dice_sum
    next_player()

def quit_to_os() -> None:
    """Exit from game"""
    print("Thank you. Take a good day.")
    sys.exit()

def put_aside() -> None:
    """Put aside some dice if possible"""
    hold_dice = gamestat_dict['dice_list']
    hold_dice_len = len(hold_dice)
    if hold_dice_len > 0:
        print("\nYou can put aside some dice.\n")
        print("Current dices:    {}".format(hold_dice))
        hold_dice_len += 1
        number_list = list(range(1, hold_dice_len))
        print("Number of dices:  {}".format(number_list))
        print("Enter the numbers of the dices through the space to remove them.")
        user_choice = (input("Enter the space bar - hold all dices....")).strip()
        user_choice = user_choice.split(" ")
        print(user_choice)
        user_choice = sorted(user_choice)
        print(user_choice)
        count_dice_outside = len(user_choice)
        if count_dice_outside > (hold_dice_len - 1) or user_choice == ['']:
            print("You can't remove more dices than you have.")
            return
        set_user_choice = set(list(map(int, user_choice)))
        if not set_user_choice.issubset(set(number_list)):
            print("You can't remove this dice.")
            return
        while count_dice_outside > 0:
            hold_dice.pop((int(user_choice.pop()))-1)
            count_dice_outside -= 1
        print(hold_dice)
    else:
        print("You can't hold something.")

def roll_dice6d() -> None:
    """Game dice 6d"""
    number = 5 - len(gamestat_dict['dice_list'])
    try_roll = gamestat_dict['try_roll']
    print("Roll the dices...")
    new_list = []
    for i in range(0, number):
        dice_number = randint(1, 6)
        new_list.append(dice_number)
    print(new_list)
    try_roll += 1
    gamestat_dict['try_roll'] = try_roll
    gamestat_dict['dice_list'] = gamestat_dict['dice_list'] + new_list
    print(gamestat_dict['dice_list'])
    print(try_roll)

def bonus() -> None:
    """Count bonus"""
    position = int(gamestat_dict['semaphore'])
    if gamestat_dict['bonus'][position] is not None:
        return
    bonus_sum = 0
    position = int(gamestat_dict['semaphore'])
    bonus_list = ['three_kind', 'four_kind', 'full_house', 'sstraight',
                  'lstraight', 'yacht', 'chance']
    for num in bonus_list:
        if gamestat_dict[num][position]:
            bonus_sum += int(gamestat_dict[num][position])
    if bonus_sum > 63:
        gamestat_dict['bonus'][position] = 35

def total() -> None:
    """Count total"""
    position = int(gamestat_dict['semaphore'])
    position = int(gamestat_dict['semaphore'])
    total_sum = 0
    full_list = ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes',
                 'bonus', 'three_kind', 'four_kind', 'full_house', 'sstraight',
                 'lstraight', 'yacht', 'chance']
    for num in full_list:
        if gamestat_dict[num][position]:
            total_sum += int(gamestat_dict[num][position])
    gamestat_dict['total'][position] = total_sum

def next_player() -> None:
    """turn move to next player"""
    bonus()
    total()
    gamestat_dict['try_roll'] = 0
    gamestat_dict['dice_list'] = []
    if gamestat_dict['semaphore'] == 0:
        gamestat_dict['semaphore'] = 1
    else:
        gamestat_dict['semaphore'] = 0

action_dict = {'1': check_top_field,
               '2': check_top_field,
               '3': check_top_field,
               '4': check_top_field,
               '5': check_top_field,
               '6': check_top_field,
               'T': three_of_kind,
               'F': four_of_kind,
               'H': full_house,
               'S': check_small_straight,
               'L': check_large_straight,
               'Y': check_yahtzee,
               'C': check_chance,
               'W': watch_game_rules,
               'Q': quit_to_os,
               'P': put_aside,
               'R': roll_dice6d}

show_board(gamestat_dict)
while True:
    if gamestat_dict['semaphore'] == 0:
        print("Player1, Make you choice...")
    else:
        print("Player2, Make you choice...")
    choice = getch().upper()
    if choice == 'R' or choice == 'P':
        if gamestat_dict['try_roll'] == 3:
            show_board(gamestat_dict)
            print("Make choice. No more dice rolls this turn.")
        else:
            print(choice)
            choice = action_dict[choice]
            choice()
            show_board(gamestat_dict)
    elif choice in ['1', '2', '3', '4', '5', '6']:
        check_number = int(choice)
        choice = action_dict[choice]
        choice(check_number)
        show_board(gamestat_dict)
    elif choice in action_dict.keys():
        print(choice)
        choice = action_dict[choice]
        choice()
        show_board(gamestat_dict)
    else:
        print("Enter avalibal command")
