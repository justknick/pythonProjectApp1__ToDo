# Create a program that:
# 1. Prompts the user to input a (dollar) amount.
# 2. Calculates the corresponding amount in euros, given an exchange rate of 2.
# 3. Prints out the amount in euros.

rate = 2

amount = float(input("Enter US Dollar amount: $"))
amount_eur = amount * rate
print("In euros, its: ", amount_eur)
