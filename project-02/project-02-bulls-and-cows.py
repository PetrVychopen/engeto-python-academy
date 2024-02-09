"""
projekt_02-text-analyzer.py: druhý projekt do Engeto Online Python Akademie

author: Petr Vychopeň
email: vychopen.petr@gmail.com
discord: Petr V. Psycholino#0224
"""

import random
import os

# Clear screen
os.system('cls')

# Random number generator
def generate_secret_number():
    digits = random.sample(range(1, 10), 4)
    result = ''
    for digit in digits:
        result += str(digit)
    return result

separator = 47 * '-'

print("Hi there!")
print(separator)
print("I've generated a random 4-digit number for you.")
print("Let's play a bulls and cows game.")
print(separator)

secret_number = generate_secret_number()
print("Secret number:", secret_number)

# Initialize attempt counter
attempts = 0

while True:
    # User prompt
    guess = input("Enter a number: ")
    attempts += 1

    # Validity check for guessed number
    if not guess.isdigit() or len(guess) != 4 or len(set(guess)) \
        != 4 or guess[0] == '0':
        print("Enter a 4-digit unique numbers not starting with 0.")
        continue

    # Calculate bulls
    bulls = 0
    for s, g in zip(secret_number, guess):
        if s == g:
            bulls += 1

    # Calculate cows
    cows = 0
    for digit in set(guess):
        cows += min(secret_number.count(digit), guess.count(digit))
    cows -= bulls

    # Display statistics of guessed number
    print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, "
          f"{cows} {'cow' if cows == 1 else 'cows'}")

    # Check for correct guess
    if bulls == 4:
        print(f"Correct! You've guessed the right number in "
              f"{attempts} {'guess' if attempts == 1 else 'guesses'}!")
        break

# Print a win message
if attempts == 1:
    print("Amazing!")
elif attempts <= 4:
    print("Great!")
elif attempts <= 7:
    print("Good!")
elif attempts <= 10:
    print("Average.")
else:
    print("What..?")
