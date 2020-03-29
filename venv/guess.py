import sys
import random
import utility

try:
    lowest_number = sys.argv[1]
    highest_number = sys.argv[2]
except IndexError:
    lowest_number = 1
    highest_number = 10

if utility.is_int(lowest_number) and utility.is_int(highest_number):
    number_to_guess = random.randint(int(lowest_number), int(highest_number))
else:
    print('The game accepts only numbers as parameters. Quiting the game......')
    exit(400)


def is_guessed(guess_num):
    global counter
    if int(guess_num) == number_to_guess:
        print(f'You\'re a genius! It was {guess_num}! It took you only {counter} guesses. '
              f'How did you do that!?')
        return True
    else:
        return False


if __name__ == '__main__':
    print('Welcome to Guess The Number Game!')
    print(f'You need to guess a number between {lowest_number} and {highest_number}')
    guess = input('Please enter your guess: ')
    counter = 1
    running = True
    while running:
        if utility.is_int(guess):
            if is_guessed(guess):
                running = False
            else:
                guess = input('Wrong number. Try again: ')
                counter += 1
        else:
            guess = input('Please enter only numbers: ')
