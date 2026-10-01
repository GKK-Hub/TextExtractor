import re
def phone_extractor(file):
    with open('records.txt', 'r') as file:
        records = file.read()  # str object
        phone_pattern = r"Phone:\s*(\+91\s?\d{10})"
        phone_no = refindall(phone_pattern,string=records)
    return phone_no
print(phone_extractor('records.txt'))