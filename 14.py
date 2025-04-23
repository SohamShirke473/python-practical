ch = input("Enter a character: ")

if ch.isdigit():
    print("It is a digit.")
elif ch.islower():
    print("It is a lowercase character.")
elif ch.isupper():
    print("It is an uppercase character.")
else:
    print("It is a special character.")
