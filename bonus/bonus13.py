"""
This code is an introduction to the concept of decoupling functions in python and other programming languages.
This code gets the input in feet from a user and converts it to meter
The initial convert function alone does too much. So we will decouple it.
"""
feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters.")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")
