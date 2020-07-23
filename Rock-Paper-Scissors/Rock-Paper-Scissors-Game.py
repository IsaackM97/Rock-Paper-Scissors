import random
import math


def game_choice():
    player = input("Pick your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    player = player.lower()

    cpu = random.choice(['r', 'p', 's'])

    if player == cpu: # if the inputs are the same ('r','r' or 's','s' or 'p', 'p')
        return 0, player, cpu  # result is 0, player's input ('r','p', or 's') , cpu's input ('r','p', or 's')

    if has_won(player, cpu):
        return 1, player, cpu  # result is 1, player's input ('r','p', or 's') , cpu's input ('r','p', or 's')
        # #player won

    return -1, player, cpu  # result is -1, player's input ('r','p', or 's') , cpu's input ('r','p', or 's')
    # #computer won

def has_won(player, opponent): # opponent is the computer
    # return true is the player beats the opponent
    # To win: rock > scissors, scissors > paper, paper > rock
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    # play against the computer until someone wins best of n games
    # to win, you must win half of them by using the math function ceil(n/2)  (2/3, 3/5) games

    player_wins = 0  # player's number of wins
    cpu_wins = 0  # computer's number of wins

    wins_needed = math.ceil(n/2)

    while player_wins < wins_needed and cpu_wins < wins_needed:
        result, player, cpu = game_choice()  # calls game_choice function

        # tie
        if result == 0:
            print(f'It is a tie. You and the computer have both chosen {player}.\n')

        # Player has won
        elif result == 1:
            player_wins += 1  # player just won
            print(f'You chose {player} and the computer chose {cpu}. You won!\n')
        else:
            cpu_wins += 1  # computer just won
            print(f'You chose {player} and the computer chose {cpu}. You lost!\n')

    if player_wins > cpu_wins:
        print(f'You have won best out of {n} games! Awesome!')
    else:
        print(f'Oh man!, the computer won best out of {n} games. Try to win!')


print(play_best_of(3))