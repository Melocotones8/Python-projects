user_choice = -1

zadania = []

def pokaż_zadania():
    index_zadania = 0
    for zadanie in zadania:
        print(zadanie + " [" + str(index_zadania) + "]")
        index_zadania += 1

def dodaj_zadanie():
    zadanie = input("Wpisz treść zadania: ")
    zadania.append(zadanie)
    print("Dodano zadanie")

def usuń_zadanie():
    index_zadania = int(input("Podaj indeks zadania do usunięcia: "))
    if index_zadania < 0 or index_zadania > len(zadania) - 1:
        print("Brak zadań o wskazanym indeksie")
        return
    
    zadania.pop(index_zadania)
    print("Usunięto zadanie")

def zapisz_zadanie_w_pliku():
    file = open("zadania.txt", "w")
    for zadanie in zadania:
        file.write(zadanie+"\n")
    file.close()

def wczytaj_zadania_z_pliku():
    try:
        file = open("zadania.txt")

        for line in file.readlines():
            zadania.append(line.strip())

        file.close()
    except FileNotFoundError:
        return

wczytaj_zadania_z_pliku()


while user_choice != 5:
    if user_choice == 1:
        pokaż_zadania()

    if user_choice == 2:
        dodaj_zadanie()

    if user_choice == 3:
        usuń_zadanie()

    if user_choice == 4:
        zapisz_zadanie_w_pliku()

    if user_choice > 5 or user_choice < 1:
        print("Wybierz poprawną cyfrę")

    print()
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz w pliku")
    print("5. Zamknij program")

    print()
    user_choice = int(input("Wybierz co robimy: "))
    print()