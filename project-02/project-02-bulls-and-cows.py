"""
project-02-bulls-and-cows.py: druhý projekt do Engeto Online Python Akademie

author: Petr Vychopeň
email: vychopen.petr@gmail.com
discord: Petr V. Psycholino#0224
"""

import random

def generate_secret_number():
    digits = random.sample(range(1, 10), 4)
    return ''.join(map(str, digits))

def evaluate_guess(secret, guess):
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(min(secret.count(digit), guess.count(digit)) for digit in set(guess))
    cows -= bulls
    return bulls, cows

def is_valid_guess(guess):
    if not guess.isdigit():
        return False
    if len(guess) != 4:
        return False
    if len(set(guess)) != 4:
        return False
    if guess[0] == '0':
        return False
    return True

def main():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

    secret_number = generate_secret_number()
    # Uncomment the line below to see the secret number (for testing purposes)
    print("Secret number:", secret_number)

    attempts = 0
    while True:
        guess = input("Enter a number: ")
        attempts += 1

        if not is_valid_guess(guess):
            print("Invalid guess. Please enter a 4-digit number with unique digits and not starting with 0.")
            continue

        bulls, cows = evaluate_guess(secret_number, guess)
        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

        if bulls == 4:
            print(f"Correct, you've guessed the right number\nin {attempts} {'guess' if attempts == 1 else 'guesses'}!")
            break

    # Print a message based on the number of attempts
    if attempts == 1:
        print("That's amazing!")
    elif attempts <= 4:
        print("That's great!")
    elif attempts <= 7:
        print("That's good!")
    elif attempts <= 10:
        print("That's average.")
    else:
        print("That's not so good.")

if __name__ == "__main__":
    main()
