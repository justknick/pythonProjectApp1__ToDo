import csv

with open("weather.csv", 'r') as file:
    data = list(csv.reader(file))

# print(data)

city = input("Enter a City: ")

for row in data[1:]:
    # print(row)
    if row[0] == city:
        print("Tempuerature is " + row[1])
    # else:
        # print("No match found. ")