print("""This program is an implementation of the Rosenberg
    Self-Esteem Scale. This program will show you ten
    statements that you could possibly apply to yourself.
    Please rate how much you agree with each of the
    statements by responding with one of these four letters:\n
    D means you strongly disagree with the statement.
    d means you disagree with the statement.
    a means you agree with the statement.
    A means you strongly agree with the statement.\n""")

points = 0

#Begin questions
def positive_score(choice):
    global points

    if choice == "D":
        points = points + 0
    elif choice == "d":
        points = points + 1
    elif choice == "a":
        points = points + 2
    elif choice == "A":
        points = points + 3
    else:
        print("It is not an option")

def negative_score(choice):
    global points
    if choice == "D":
        points = points + 3
    elif choice == "d":
        points = points + 2
    elif choice == "a":
        points = points + 1
    elif choice == "A":
        points = points + 0
    else:
        print("It is not an option")


def positive_question(question):
    choice = input(f"{question} \n    Enter D, d, a, or A: ")
    positive_score(choice)

def negative_question(question):
    choice = input(f"{question} \n    Enter D, d, a, or A: ")
    negative_score(choice)

def main():
    positive_question("I feel that I am a person of worth, at least on an equal plane with others.")
    positive_question("I feel that I have a number of good qualities.")
    negative_question("All in all, I am inclined to feel that I am a failure.")
    positive_question("I am able to do things as well as most other people.")
    negative_question("I feel I do not have much to be proud of.")
    positive_question("I take a positive attitude toward myself.")
    positive_question("On the whole, I am satisfied with myself.")
    negative_question("I wish I could have more respect for myself.")
    negative_question("I certainly feel useless at times.")
    negative_question("At times I think I am no good at all.")

    print(f"Your score is {points}")
    print("A score below 15 may indicate problematic low self-esteem.")

if __name__ == "__main__":
    main()
