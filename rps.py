import time
import random


def countdown(moves):
    """"Rock, Paper, Scissors, Shoot!" countdown"""
    for i in moves:
        print(i)
        time.sleep(0.5)
    print('Shoot!')


def choices(moves):
    user_move = int(input('\nRock (0), paper (1) or scissors (2)? '))
    if user_move not in [0, 1, 2]:
        input('\nPlease choose 0, 1 or 2. Press enter to try again.')
        choices(moves)
    user_move = moves[user_move]
    time.sleep(0.5)
    print(f'\nYou chose {user_move}.')

    cpu_move = moves[random.randint(0, 2)]
    time.sleep(1)
    print(f'Your opponent chose {cpu_move}')

    results = [user_move, cpu_move]
    return results


def did_player_win(user_move, cpu_move):
    """Determines the winner based on the chosen moves"""
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


def print_stats(stats):
    """Print user wins/losses"""
    time.sleep(1)
    print()
    for k, v in stats.items():
        print(f'{k}: {v}')


def main():
    """Main game loop"""
    print('\nWelcome to rock, paper scissors.')
    time.sleep(0.5)
    name = input('\nWhat is your name? ')
    time.sleep(0.5)
    print(f'Hi, {name}.\n')

    moves = ['Rock', 'Paper', 'Scissors']
    stats = {'Wins': 0, 'Losses': 0, 'Draws': 0}

    play = True
    while play:
        # Countdown and apply selections
        input('Press enter to play! \n')
        countdown(moves)
        results = choices(moves)

        # Check for draw, add to and print stats and ask for rematch
        if results[0] == results[1]:
            time.sleep(1)
            print('\nIt\'s a draw!')
            stats['Draws'] += 1

            print_stats(stats)
            play = int(input('\nPlay again? Yes (1), No (0) \n'))
            if play:
                continue
            else:
                break

        # Check if player won, add to and print stats, ask for rematch
        player_won = did_player_win(results[0], results[1])
        if player_won:
            time.sleep(1)
            print('You won!')
            stats['Wins'] += 1
        else:
            time.sleep(1)
            print('You lost :(')
            stats['Losses'] += 1

        print_stats(stats)
        play = int(input('\nPlay again? Yes (1), No (0) \n'))

    print('Bye, thanks for playing!')


if __name__ == "__main__":
    main()
