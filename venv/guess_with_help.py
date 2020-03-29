import random
import sys
import utility

running = True

lowest_number = sys.argv[1]
highest_number = sys.argv[2]

if utility.is_int(lowest_number) and utility.is_int(highest_number):
    number_to_guess = random.randint(int(lowest_number), int(highest_number))
else:
    print('The game accepts only numbers as parameters. Quiting the game......')
    exit(400)

print('Welcome to Guess The Number Game!')
print(f'You need to guess a number between {lowest_number} and {highest_number}')
guess = input('Please enter your guess: ')
counter = 1

while running:
    if utility.is_int(guess):
        if int(guess) == number_to_guess:
            print(f'You\'re a genius! It was {guess}! It took you only {counter} guesses. '
                  f'How did you do that!?')
            running = False
        elif int(guess) < number_to_guess:
            guess = input('Wrong number. The number is bigger. Try again: ')
            counter += 1
        else:
            guess = input('Wrong number. The number is smaller. Try again: ')
            counter += 1
    else:
        guess = input('Please enter only numbers: ')