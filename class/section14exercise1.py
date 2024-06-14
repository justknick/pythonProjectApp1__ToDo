# Define a get_age function that:
# 1. has two parameters, year_of_birth and current_year .
# 2. the current_year  parameter should be a default parameter.
#    The default value should be the current year.
# 3. the function should calculate and return the age of the user
#    given the year_of_birth and the current_year.
def get_age(year_of_birth_arg, current_year_arg=2023):
    age = current_year_arg - year_of_birth_arg
    return age


get_age(1989)
