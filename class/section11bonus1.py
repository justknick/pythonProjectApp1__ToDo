try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    if width == length:
        exit("That looks like a square. ")

    area = width * length
    print(area)

except ValueError:
    # No 'continue' needed bc we're not in a loop
    print("Oh, you need to enter it as a number. ")

