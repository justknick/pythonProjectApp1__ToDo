# Your task for this exercise is to complete the strength
# function. The function is supposed to check the strength
# of the user's password.
# The function should:
# 1. get a password argument
# 2. return the string "Strong Password" if all of the following conditions are true:
# Eight or more characters
# At least one uppercase letter.
# At least one digit.
# 3. returns "Weak Password" if at least one of the three conditions is not met.
# Note:  You can make use of the code we developed in the Bonus Example on Day 9.
def strength(password):
    result = {}

    # Check Length
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    # Check Caps
    caps = False
    for i in password:
        if i.isupper():
            caps = True
    result["capitalize"] = caps

    # Check Digits
    digits = False
    for i in password:
        if i.isdigit():
            digits = True
    result["digits"] = digits

    if all(result.values()):
        message = "Strong Password"
    else:
        message = "Weak Password"

    return message
