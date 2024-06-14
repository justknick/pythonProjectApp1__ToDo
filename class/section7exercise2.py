# Take a look at the s7e3-essay.txt file tab. That file contains some text.
# You should create a program that reads the s7e3-essay.txt file, converts
# the first letter of each word to uppercase and prints out the converted text.

document = open('../files/s7e3-essay.txt', 'r')
contents = document.readlines()
document.close()
print(contents[0].title())
