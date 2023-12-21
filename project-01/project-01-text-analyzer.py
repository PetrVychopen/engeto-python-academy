"""
projekt_01-text-analyzer.py: první projekt do Engeto Online Python Akademie

author: Petr Vychopeň
email: vychopen.petr@gmail.com
discord: Petr V. Psycholino#0224
"""

# NOTE: Not the best practice (security)

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}


# TODO: asterisks while typing

user_username = str(input("Username: "))
user_password = str(input("Password: "))

if user_username in registered_users and user_password == registered_users[user_username]:
    print("ok")
else:
    print("nok")