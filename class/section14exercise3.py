# Define a function that calculates the area of a square.
# For example, if I was to call your function with foo(7) the output
# would be 49. If I called it with foo(3)  it would return 9, and so on.
# Note that you don't have to name your function foo. Give it any name you want.

def calc_area(length_arg):
    area = length_arg ** 2
    return area


print(calc_area(9))
