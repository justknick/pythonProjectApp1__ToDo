# Define a function that takes a list as an argument and returns the
# average value of the list items. For example, if I called your
# function with foo([10, 20, 30, 40]) it should return 25, the average
# of the numbers of the list.
list = [10, 20, 30, 40]

def get_average(foo_local):
    count_local = 0
    total_local = 0
    for item in list:
        count_local = count_local + 1
        total_local = total_local + item
    average_local = total_local / count_local
    return average_local


print(get_average(list))