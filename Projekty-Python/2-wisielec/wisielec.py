import string
import random

no_of_tries = 5
words = []
used_letters = []
litery = string.ascii_letters
user_word = []
user_choice = -1

def load_file():
    file = open("wisielec.txt")
    for lines in file.readlines():
        words.append(lines.strip())
    file.close()

load_file()

# print(words)

word = random.choice(words)

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
        
    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Pozostało prób:", no_of_tries)
    print("Użyte litery:", used_letters)
    print()

for letter in word:
    user_word.append("_")

def gra():
    while True:
        global no_of_tries
        letter = input("Podaj literę: ")
            
        if litery.count(letter) == 1:
                used_letters.append(letter)
        else:
            print()
            print("Należy podać literę")

        found_indexes = find_indexes(word, letter)

        if len(found_indexes) == 0 and litery.count(letter) == 1:
            print("Nie ma takiej litery")
            no_of_tries -= 1
            if used_letters.count(letter) == 2:
                print("Ta litera została już użyta!")
                used_letters.pop()
                no_of_tries += 1

                # print("Pozostałe próby:", no_of_tries)
        elif used_letters.count(letter) == 2:
            print("Ta litera została już użyta!")
            used_letters.pop()

            if no_of_tries == 0:
                print("Game over")
                return
                
        else:
            for index in found_indexes:
                user_word[index] = letter
                # print(user_word)
                
            if "".join(user_word) == word:
                print(user_word)
                print("Brawo!")
                words.remove(word)
                no_of_tries ==5
                return

        show_state_of_game()

def poziom_trudnosci():
    global no_of_tries
    print()
    print("1. Izi (8 żyć)")
    print("2. Medium (5 żyć - domyślnie)")
    print("3. Hard (3 życia)")
    print()
    poziom = int(input("Który poziom wybierasz? "))
    
    if poziom == 1:
            no_of_tries = 8
    if poziom == 2:
            no_of_tries = 5
    if poziom == 3:
            no_of_tries = 3
    if poziom > 3 or poziom < 1:
            print()
            print("Wybierz cyfrę od 1 do 3!")
            return

def dodaj_slowo():
    imie = input("Podaj imię bez polskich znaków: ")
    words.append(imie)
    file = open("wisielec.txt", "w")
    for imie in words:
         file.write(imie+"\n")
    file.close

def lista_imion():
     print("Imiona: ", words)

while user_choice != 5:

    if user_choice == 1:
        gra()

    if user_choice == 2:
        poziom_trudnosci()

    if user_choice == 3:
         dodaj_slowo()

    if user_choice == 4:
         lista_imion()

    print()
    print("1. Gramy!")
    print("2. Wybierz poziom trudności")
    print("3. Dodaj nowe słowo")
    print("4. Pokaż listę imion")
    print("5. Wyłącz grę")
    print()
    print("liczba żyć: ", no_of_tries)

    print()
    user_choice = int(input("Co robimy? "))
    print()