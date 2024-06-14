# Create a program that prompts the user to input their name once.
# Then, the program repeatedly prints out the name with the first
# letter capitalized.

user_input = input("Input your name once: ")
while True:
    print(user_input.capitalize())
