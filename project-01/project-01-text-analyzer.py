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

split_text = TEXTS[int(selected_number) -1].split()

word_counter = len(split_text)

titlecase_counter = 0
for word in split_text:
    if word.istitle():
        titlecase_counter += 1

lowercase_counter = 0
for word in split_text:
    if word.islower():
        lowercase_counter += 1

uppercase_counter = 0
for word in split_text:
    if word.isupper() and word.isalpha():
        uppercase_counter += 1

numeric_counter = 0
for word in split_text:
    if word.isnumeric():
        numeric_counter += 1

numeric_list = []
for word in split_text:
    if word.isnumeric():
        numeric_list.append(int(word))
numeric_sum = sum(numeric_list)

print(f"There are {word_counter} words in the selected text.")
print(f"There are {titlecase_counter} titlecase words.")
print(f"There are {uppercase_counter} uppercase words.")
print(f"There are {lowercase_counter} lowercase words.")
print(f"There are {numeric_counter} numeric strings.")
print(f"The sum of all the numbers {numeric_sum}.")