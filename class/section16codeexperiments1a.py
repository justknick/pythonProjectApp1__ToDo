import glob


myFiles = glob.glob("files/s16*.txt")


# iterate over filepath
for filepath in myFiles:
    # with each filepath, apply the open function
    with open(filepath, 'r') as file:
        print(file.read())
