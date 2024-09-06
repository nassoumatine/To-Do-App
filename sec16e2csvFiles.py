# We learn about.csv files

import csv
with open("weather.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data[1:]:
    if row[0] == city.title():
        print(row[1])
