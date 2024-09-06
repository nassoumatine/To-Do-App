"""
This code creates a function that gets some numbers from a text file and returns the average of those numbers
"""


def get_average():
    with open("files/data.txt", 'r') as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)
    return average_local


average = get_average()
print(average)
