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

separator = 40 * "-"

if user_username in registered_users and \
    user_password == registered_users[user_username]:
    
    print(separator)
    print("Welcome to the app, bob", "We have 3 texts to be analyzed.", sep="\n")
    print(separator)
else:
    print("unregistered user, terminating the program..")
    quit()

selected_number = int(input("Enter a number btw. 1 and 3 to select:"))

if selected_number is not int() and selected_number not in range(1, 4):
    print("Wrong input. Select number 1, 2 or 3.")
    quit()


print(separator)