# Write a get_nr_items function that:
# 1. gets one parameter. The parameter is expected to be a list of strings.
# 2. returns the number of items the list contains.
def get_nr_items(items_arg):
    this_list = items_arg.split(',')
    volume = len(this_list)
    return volume


my_items = 'apple,banana,orange'
result = get_nr_items(my_items)
print(result)
