import re

url = input("Enter a URL: ")

url_pattern = r'^(https?://)?(www\.)?[\w-]+(\.[\w-]+)+(/[\w\-./?%&=]*)?$'

if re.fullmatch(url_pattern, url):
    print("Valid URL.")
else:
    print("Invalid URL.")
