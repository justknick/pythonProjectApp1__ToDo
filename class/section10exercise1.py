# Write a program that:
# 1. asks users to enter a password.
# 2. returns "Great password there!" if the password has more than 7 characters.
# 3. returns "Your password is weak." if the password has 7 or fewer characters.
password = input("Enter a password: ")

# Check for character length
if len(password) > 7:
    print("Great password there!")
else:
    print("Your password is weak.")
