import re

with open("data.txt", "r") as file:
    text = file.read()

email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
phone_pattern = r'\+?\d{10,15}'
date_pattern = r'\b\d{2}/\d{2}/\d{4}\b'

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)
dates = re.findall(date_pattern, text)

print("Emails:", emails)
print("Phone Numbers:", phones)
print("Dates:", dates)
