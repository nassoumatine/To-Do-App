"""
This code is an introduction to the concept of decoupling output in python and other programming languages.
This code gets the input in feet from a user and converts it to meter
"""
feet_inches = input("Enter feet and inches: ")


def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters  # f"{feet} feet and {inches} inches is equal to {meters} meters."


result = convert(feet_inches)
if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")

# We will tackle the fact that we want line 14 to be printed before 19/21 later.
