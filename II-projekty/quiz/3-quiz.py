import json

points = 0
answers = ['a', 'b', 'c', 'd']

def show_question(question):
    global points
    global answers

    print()
    print(question["pytanie"])
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    print()

    answer = input("Która odpowiedź jest prawidłowa? ")

    if answers.count(answer) != 1:
        while answers.count(answer) != 1:
            print("Należy wybrać 'a', 'b', 'c' lub 'd'")
            answer = input("Podaj wartość ponownie: ")

    if answer == question["prawidlowa_odpowiedz"]:
            points += 1
            print("To prawidlowa odpowiedz, masz już ", points, "punktów.")

    else:
        print("Błędna odpowiedź, prawidłowa to " + question["prawidlowa_odpowiedz"] + ".")

with open("2-quiz.json") as json_file:
    questions = json.load(json_file)

    for i in range(0, len(questions)):
        show_question(questions[i])

print()
print("To koniec gry, punty: " + str(points))