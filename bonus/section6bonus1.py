waiting_list = ['sen', 'ben', 'john']

# reverse = True argument in the sort function will sort list in descending order
waiting_list.sort(reverse=False)

for index, item in enumerate(waiting_list):
    print(f"{index + 1}. {item.capitalize()}")
