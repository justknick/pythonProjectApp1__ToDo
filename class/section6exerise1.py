elements = ['a', 'b', 'c']
elements[1] = 'x'
# print(elements)

for index, item in enumerate(elements):
    print(f"{index + 1}. {item}")
