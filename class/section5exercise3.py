# This time you should create a program that:
# 1. Contains the above list.
# 2 Prompts the user to input the person's name.
# 3. Returns the rank that person has.

ranking = ['John', 'Sen', 'Lisa']

for ranked in ranking:
    print(ranked.title())

user_input = input("Enter candidate: ").strip()

match user_input.capitalize():
    case "John":
        print(ranking.index(user_input.capitalize())+1)
    case "Sen":
        print(ranking.index(user_input.capitalize())+1)
    case "Lisa":
        print(ranking.index(user_input.capitalize())+1)
    case _:
        print("Try again.")
