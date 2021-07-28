"""
Created By : Md Ashfaque
"""

import random
import sys


# # Number of Snakes with Head and Tail
snakes = {16:4, 22:10, 33:20, 48:24, 62:56, 78:69, 74:60, 91:42, 97:6}
# snakes = {}
# number_of_snakes = int(input("Enter number of snakes : "))
# count = 1
# while count <= number_of_snakes:
#     head = int(input("Enter head : "))
#     tail = int(input("Enter tail : "))
#     snakes[head] = tail
#     count += 1

# print(snakes)

# # Number of Ladders with bottom and top position
ladders = {3:12, 7:23, 11:25, 21:56, 47:53, 60:72, 80:96}
# ladders = {}
# number_of_ladders = int(input("Enter number of Ladders : "))
# count_l = 1
# while count_l <= number_of_ladders:
#     bottom_pos = int(input("Enter bottom position : "))
#     top_pos = int(input("Enter top position : "))
#     ladders[bottom_pos] = top_pos
#     count_l += 1

# print(ladders)

# ACCEPTING NUMBER OF PLAYERS
# dp = []
def players_count():
    num_of_players = int(input("How many players are playing the game : "))
    # global dp
    # dp = [False]*num_of_players
    # if num_of_players > 4:
    #     print("For now we support 4 players!")
    # elif num_of_players < 2:
    #     print("There is no enjoyment in playing alone!")
    # else:
    #     print(num_of_players)
    #     return num_of_players
    return num_of_players


# ACCEPTING NAMES OF PLAYERS
def name_of_players(N):
    # names = ['', '', '', '']
    names = ["" for i in range(N)]
    for i in range(N):
        names[i] = input("Enter name of Player " + str(i+1) + " : ")
    return names

# THIS FUNCTION MOVES THE PIECE AND ALSO CHECKS FOR WINNING AND 
# OVERFLOW
def move(player, value):
    roll_dice = random.randint(1, 6)
    num = value + roll_dice
    if num > 100:
        print(f"BAD LUCK, YOU CANT MOVE, YOU NEED {100 - value} TO WIN")
        return value

    if num == 100:
        return num

    # IF PLAYER IS NOT REACHED HOME
    print(player, "Rolled a ", roll_dice, " and moved from", value, " to ", num)

    # TO CHECK IF PIECE STOPPED ON SNAKE HEAD
    if num in snakes:
        print(player, " got bitten by a snake and is now on", snakes[num])
        num = snakes[num]

    # IF PLAYER IS ON LADDER BOTTOM IT WILL CLIMB THE LADDER
    elif num in ladders:
        print(player, "Climbed the ladder and is now on ", ladders[num])
        num = ladders[num]

    return num


def turn(player, pos):
    play_message = "Press Enter to continue or press 'stop' to stop : "
    win_message = "WINS THE GAME! CONGRATULATIONS"
    player_turn_message = str("Hey " + player + " ! It's your turn now " + play_message)
    player_input = input(player_turn_message)

    # IF THE USER CHOSE TO QUIT GAME, THE GAME MUST STOP
    if player_input.lower() == 'stop':
        return True, pos

    pos = move(player, pos)
    
    # IF THE PLAYER WINS, THE GAME SHOULD BE OVER
    if pos == 100:
        print(player, win_message)
        print(f"AT WINNING {player} was at {pos}")
        # player = "winner"
        return True, pos

    # IF PLAYER HAS NOT QUIT THE GAME AND ALSO HE HAS NOT REACHED HOME
    # THE GAME SHOULD CONTINUE
    return False, pos




# THE MAIN FUNCTION
def main_function():
    num_of_players = players_count()
    players_names = name_of_players(num_of_players)
    # print(players_names[0], players_names[1], players_names[2], 
    # players_names[3], " - Welcome to Snakes and Ladders")
    for i in players_names:
        print(i, end=" ")
    print(" - Welcome To Snakes and Ladders")

    player_turn = 0
    # player_positions = [0, 0, 0, 0]
    player_positions = [0 for i in range(num_of_players)]

    # TO CHECK WHETHER THE GAME SHOULD CONTINUE OR NOT
    game_over = False
    while not game_over:
        # 
        while player_turn < num_of_players:
            player_turn += 1
            game_over, player_positions[player_turn-1]= turn(players_names[player_turn-1], player_positions[player_turn-1])
            if game_over:
                return
        player_turn = 0
    return

    # trying to implement the functionality of playing game till the last player
    # game_over = False
    # p1 = False
    # while not game_over:
    #     while player_turn < num_of_players:
    #         player_turn += 1
    #         player = ''
    #         winner_count = 0
    #         if player_positions[player_turn-1] == 100 and players_names[player_turn-1] == 'winner':
    #             winner_count += 1
    #             continue
    #         else:
    #             game_over, player_positions[player_turn-1], player = turn(players_names[player_turn-1], player_positions[player_turn-1], player_turn-1)

    #         if len(players_names) - winner_count == 1:
    #             game_over = True
    #     player_turn = 0
    # return


if __name__=='__main__':
    main_function()
