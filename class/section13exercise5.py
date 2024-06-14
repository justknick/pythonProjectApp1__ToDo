# Implements a function that takes two strings as parameters,
# concatenates them and returns the result.
name_first = 'John'
name_last = 'Doe'

def concatenate_two(input_one, input_two):
    result = {input_one, input_two}
    new_string = ''.join(result)
    return new_string

print(concatenate_two(name_first, name_last))
