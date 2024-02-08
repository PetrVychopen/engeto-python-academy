"""
projekt_02-text-analyzer.py: druhý projekt do Engeto Online Python Akademie

author: Petr Vychopeň
email: vychopen.petr@gmail.com
discord: Petr V. Psycholino#0224
"""

import random

def generate_secret_number():
    digits = random.sample(range(1, 10), 4)
    return ''.join(map(str, digits))

# Old version of secret number generator

# def generate_secret_number():
#     digits = random.sample(range(1, 10), 4)
#     result = ''
#     for digit in digits:
#         result += str(digit)
#     return result

print("Hi there!")
print("-----------------------------------------------")
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-----------------------------------------------")

secret_number = generate_secret_number()
print("Secret number:", secret_number)

# Init for attempt counter
attempts = 0

while True:

    # User prompt
    guess = input("Enter a number: ")
    attempts += 1

    # Validity check for guessed number
    if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4 \
            or guess[0] == '0':
        print("Invalid guess. Please enter a 4-digit number with unique "
              "digits and not starting with 0.")
        continue

    # Evaluation of guessed number
    bulls = sum(1 for s, g in zip(secret_number, guess) if s == g)
    cows = sum(min(secret_number.count(digit), guess.count(digit)) \
               for digit in set(guess))
    cows -= bulls

    # Statistics of guessed number
    print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} "
          f"{'cow' if cows == 1 else 'cows'}")

    # Check for "bullseye"
    if bulls == 4:
        print(f"Correct, you've guessed the right number\nin {attempts} "
              f"{'guess' if attempts == 1 else 'guesses'}!")
        break