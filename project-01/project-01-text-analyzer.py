"""
projekt_01-text-analyzer.py: první projekt do Engeto Online Python Akademie

author: Petr Vychopeň
email: vychopen.petr@gmail.com
discord: Petr V. Psycholino#0224
"""
"""
Co by jsi měl/a zlepšit:
[x] řádek 43 a 44: zbytečně převádíš input, který už je string znovu na string
[] při ověření uživatele bych trochu více rozepsal podmínky pro chyby jako 
    špatné heslo, špatný username místo pouze jednoho else
[x] řádek 62 a podmínka in range(1,4), tady je mnohem lepší místo pevně dané 
    4ky pracovat s délkou listu TEXTS, protože kód potom bude fungovat vždy pro 
    všechny texty v tom listu. Například kdyby ti někdo do toho listu přidal 
    dalších 100 textů, protože je chce analyzovat, tak tvůj kod by fungoval vždy 
    p  ouze pro čtyři a musel bys přepsat kód. V nejlepším případě chceme vše 
    automatizovat a vyhnout se manuálnímu nebo pevně daném přiřazování, takže 
    použít délku listu do podmínky + všech printů kde pracuješ s počtem textů
[] chybí mi čištění slov od znaků nějakou metodou jako strip, aby ses zbavil 
    čarek za slovy. Split tohle neřeší a potom ty výsledky nejsou úplně přesné
[] používáš několikrát furt ten samý for loop, což se nabízí použít pouze 
    jednou a všechno to sčítání si řídit přes podmínky. Tímto způsobem bude kód 
    asi 5x rychlejší, protože nebude 5x procházet ten stejný loop a kód bude 
    mnohem kratší a přehlednější
[x] pokud používáš funkce, tak funkce musí být definovány nahoře před hlavním 
    chodem kódu a né uprostřed kódu
"""
import os

def format_table(data):
    max_len = max(len(str(item[0])) for item in data)

    print(f"{'LEN': <4}| {'OCCURRENCES': ^16}| NR.")
    print(separator)

    for item in data:
        length, occurrences = item
        print(f"{length: <4}| {'*' * occurrences: <16}| {occurrences}")

# Clear screen
os.system('cls')

# NOTE: Not the best practice (security)

from task_template import TEXTS

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}


# TODO: asterisks while typing

user_username = input("Username: ")
user_password = input("Password: ")

separator = 40 * "-"

if user_username in registered_users and \
    user_password == registered_users[user_username]:
    
    print(separator)
    print(f"Welcome to the app, {user_username}", 
          "We have 3 texts to be analyzed.", sep="\n")
    print(separator)

else:
    print("Unregistered user, terminating the program..")
    quit()


selected_number = input("Enter a number btw. 1 and 3 to select: ")
if selected_number.isdigit() and int(selected_number) in range(1, len(TEXTS)):
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

print(separator)

word_lengths = {}
for word in split_text:
    word_length = len(word)

    if word_length in word_lengths:
        word_lengths[word_length] += 1
    else:
        word_lengths[word_length] = 1

sorted_items = sorted(word_lengths.items())



format_table(sorted_items)