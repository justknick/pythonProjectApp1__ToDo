# Define a function that:
# (1) takes a temperature as a parameter
# (2) returns "Warm" if the temperature is greater than 7
# (3) returns "Cold" if the temperature is equal to or less than 7
# If I called your function with foo(10) it would return Warm.
# If I called it with foo(7) or foo(5) it would return Cold in both cases, and so on.
def temperature_check(temperature):
    message = ''
    if temperature < 7:
        message = 'Warm'
    else:
        message = 'Cold'
    return message

