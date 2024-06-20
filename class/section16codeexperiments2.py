import csv

with open("files/weather.csv", 'r') as file:
    # reader is a csv function of the csv module and expects a file object as input
    # we supply the file object to the reader function to yield an iterator object instance
    data = list(csv.reader(file))

count = 0

city = input("Enter a City: ")

for row in data[1:]:
    if row[0] == city:
        print("Temperature in " + row[0] + " is " + row[1])
        count = count + 1

# prints message when city input is not in the list
if count == 0:
    print("No matches found")
