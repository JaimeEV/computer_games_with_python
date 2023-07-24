# This is a Guess the Number game.
import random

guess_taken = 0
number = random.randint(1, 30)
lives = 6

my_name = input('Hello! What is your name?: ')
print('Well, ' + my_name + ', I am thinking of a number between 1 and 20.')

for guess_taken in range(lives):
    print('♥' * lives)
    lives -= 1
    guess = int(input('Take a guess: '))

    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    elif guess == number:
        break

if guess == number:
    guesses_taken = str(guess_taken + 1)
    print('♥' * lives)
    print('Good job, ' + my_name + '! You guessed my number in ' + guesses_taken + ' guesses!')
else:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')



