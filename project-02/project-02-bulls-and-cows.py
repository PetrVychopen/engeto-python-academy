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

print("Hi there!")
print("-----------------------------------------------")
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-----------------------------------------------")

secret_number = generate_secret_number()
print("Secret number:", secret_number)
