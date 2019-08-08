import time
import random


# Global variables
print('\nWelcome to rock, paper scissors.')
time.sleep(0.5)
name = input('\nWhat is your name? ')
time.sleep(0.5)
print(f'Hi, {name}.\n')

moves = ['Rock', 'Paper', 'Scissors']
stats = {'Wins': 0, 'Losses': 0}


# "Rock, Paper, Scissors" countdown
def countdown():
    for i in moves:
        print(i)
        time.sleep(0.5)
    print('Shoot!')


def choices():
    user_move = int(input('\nRock (0), paper (1) or scissors (2)? '))
    if user_move not in [0, 1, 2]:
        input('\nPlease choose 0, 1 or 2. Press enter to try again.')
        choices()
    user_move = moves[user_move]
    time.sleep(0.5)
    print(f'\nYou chose {user_move}.')

    cpu_move = moves[random.randint(0, 2)]
    time.sleep(1)
    print(f'Your opponent chose {cpu_move}')

    results = [user_move, cpu_move]
    return results


# Determines the winner based on the chosen moves
def did_player_win(user_move, cpu_move):
    if user_move == 'Rock' and cpu_move == 'Scissors':
        return True
    elif user_move == 'Rock' and cpu_move == 'Paper':
        return False
    elif user_move == 'Paper' and cpu_move == 'Rock':
        return True
    elif user_move == 'Paper' and cpu_move == 'Scissors':
        return False
    elif user_move == 'Scissors' and cpu_move == 'Paper':
        return True
    elif user_move == 'Scissors' and cpu_move == 'Rock':
        return False


# Print user wins/losses
def print_stats():
    for k, v in stats.items():
        print(f'{k}: {v}')


play = True

while play:
    input('Press enter to play! ')
    print()
    countdown()

    results = choices()

    is_draw = True

    while is_draw:

        if results[0] == results[1]:
            time.sleep(1)
            input('\nDraw! Press enter to countdown again. ')
            print()
            countdown()
            results = choices()
        else:
            is_draw = False

    player_won = did_player_win(results[0], results[1])
    if player_won:
        time.sleep(1)
        print('You won!')
        stats['Wins'] += 1
    else:
        time.sleep(1)
        print('You lost :(')
        stats['Losses'] += 1

    time.sleep(1)
    print()
    print_stats()

    play = int(input('\nPlay again? Yes (1), No (0) '))
    print()

print('Thanks for playing!')
