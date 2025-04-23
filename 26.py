import re

password = input("Enter your password: ")

# Validation regex
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'

if re.fullmatch(pattern, password):
    print("Password is valid.")
else:
    print("Invalid password. It must be at least 8 characters long, with uppercase, lowercase, digit, and special character.")
