# Write a program that reads the s7e3-essay.txt file and returns
# the number of characters contained in the file.

document = open('../files/s7e3-essay.txt', 'r')
contents = document.readlines()
document.close()
print(len(contents[0]))