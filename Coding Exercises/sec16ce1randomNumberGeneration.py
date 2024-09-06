"""
This program creates a program that generates a random whole number
The program first asks the user to enter a whole number for a lower bound
The program asks the user again to enter another number for an upper bound
"""
import random

# Asks the user to enter lower and upper bound
lower_bound = int(input("Enter a lower bound: "))
upper_bound = int(input("Enter an upper bound: "))

# Generates a random integer between lower_bound and upper_bound (inclusive)
output = random.randint(lower_bound, upper_bound)
print(output)
