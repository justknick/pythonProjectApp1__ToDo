from feet_inches_kid_checker import kid_checker
def notification(parsed, result):
    print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters. ")
    kid_checker(result)

