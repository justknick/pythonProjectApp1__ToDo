# We have a list of two IPs in the code area.
# Extend the code so your program:
# 1. Prompts the user to input an index (e.g., 0 or 1).
# 2. Depending on the user input, the program should return either
# You chose 100.122.133.111 or You chose 100.122.133.111
# Note: In order for the system to mark your exercise as correct,
# your code should return the exact output (i.e., upper case Y in
# You chose and no spaces or other characters after the IP.

ips = ['100.122.133.105', '100.122.133.111']

for i, item in enumerate(ips):
    print(f"{i + 1}. {item}")
number = int(input("Pick a number: "))
print(f"You chose {ips[number - 1]}")
