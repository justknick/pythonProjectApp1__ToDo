password = input("Enter new password: ")

result = {}

# Check length of password
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

# Check for numbers in password
digit = False
for  i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit

# Check for Capitals in password
caps = False
for  i in password:
    if i.isupper():
        caps = True
result["capitalize"] = caps

# print(result)
# print(result.values())
# print(result.keys())

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")