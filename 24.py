import re

# Taking input from user
phone = input("Enter phone number: ")
email = input("Enter email: ")

# Validate phone number
if re.match(r'^\d{10}$', phone):
    print("Valid Phone")
else:
    print("Invalid Phone")

# Validate email address
if re.match(r'^\S+@\S+\.\S+$', email):
    print("Valid Email")
else:
    print("Invalid Email")
