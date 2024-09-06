"""
This program checks the strength of a given password based on three conditions
"""

password = input("Enter new password: ")
result = {}

# 1. Checking if the length of the password is >= 8
if len(password) >= 8:
    result["length"] = True
else:
    result["Length"] = True
# 2. Checking if there is a number in the password
digit = False
for i in password:
    if i.isdigit():
        digit = True
result["Digit"] = digit

# 3. Checking if there is at least one upper character in the password
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["Uppercase"] = uppercase

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")



