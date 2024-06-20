date = input("Enter today's date: ")
mood = input("How'd you rate your mood (1-10 scale)? ")
entry = input("Let your thought's flow: \n")

with open(f"files/s9b1-{date}.txt", "w") as file:
    file.write(mood + 2 * '\n')
    file.write(entry)