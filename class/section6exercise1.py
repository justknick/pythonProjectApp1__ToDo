# We have a list of three strings defined in the code area.
# Extend the code so your program prints out the following out
# of that list:
# 0-Document.txt
# 1-Report.txt
# 2-Presentation.txt

filenames = ['document', 'report', 'presentation']

for i, item in enumerate(filenames):
    print(f"{i}-{item.capitalize()}.txt")