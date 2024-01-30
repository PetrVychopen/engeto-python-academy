"""
projekt_01-text-analyzer.py: první projekt do Engeto Online Python Akademie

author: Petr Vychopeň
email: vychopen.petr@gmail.com
discord: Petr V. Psycholino#0224
"""

# NOTE: Not the best practice (security)

from task_template import TEXTS

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
    print(f"Welcome to the app, {user_username}", 
          "We have 3 texts to be analyzed.", sep="\n")
    print(separator)

else:
    print("unregistered user, terminating the program..")
    quit()


selected_number = input("Enter a number btw. 1 and 3 to select:")
if selected_number.isdigit() and int(selected_number) in range(1, 4):
    print(separator)
else:
    print("Wrong input. Select number 1, 2 or 3.")
    quit()

if selected_number == '1':
    word_count = len(TEXTS[0].split())
    print(f"There are {word_count} words in the selected text.")

# Pro vybraný text spočítá následující statistiky:

# počet slov,
# počet slov začínajících velkým písmenem,
# počet slov psaných velkými písmeny,
# počet slov psaných malými písmeny,
# počet čísel (ne cifer),
# sumu všech čísel (ne cifer) v textu.

# There are 54 words in the selected text.
# There are 12 titlecase words.
# There are 1 uppercase words.
# There are 38 lowercase words.
# There are 3 numeric strings.
# The sum of all the numbers 8510