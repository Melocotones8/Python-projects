import sys
import random
import string

password = []
characters_left = -1
password_lenght = -1

def poprawne_haslo():
    global password_lenght
    global characters_left
    while password_lenght < 5:
        try:
            password_lenght = int(input("Jak długie ma być hasło? "))

            if password_lenght < 5:
                print("Hasło musi mieć co najmniej 5 znaków")
            else:
                characters_left = password_lenght
        except ValueError:
            print("Wartość musi być liczbą")


def update_characters_left(number_of_characters):
    global characters_left

    if number_of_characters < 0 or number_of_characters > characters_left:
        print("Liczba znaków spoza przedziału 0,", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print("Pozostało znaków: ", characters_left)

poprawne_haslo()

lowercase_letters = int(input("Ile małych liter ma mieć hasło? "))
update_characters_left(lowercase_letters)

uppercase_letters = int(input("Ile dużych liter ma mieć hasło? "))
update_characters_left(uppercase_letters)

special_characters = int(input("Ile znaków specjalnych ma mieć hasło? "))
update_characters_left(special_characters)

digits = int(input("Ile cyfr ma mieć hasło? "))
update_characters_left(digits)

if characters_left > 0:
    print ("Nie wszystkie znaki zostały wykorzystane. Pozostałe wolne miejsca zostaną wypełnione małymi literami")
    lowercase_letters += characters_left

print()
print("Długość hasła: ", password_lenght)
print("Duże litery:", uppercase_letters)
print("Małe litery:", lowercase_letters)
print("Znaki specjalne:", special_characters)
print("Ilość cyfr:", digits)
print()

for i in range(password_lenght):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
    digits -= 1

random.shuffle(password)
print("Wygenerowane hasło: ", "".join(password))
