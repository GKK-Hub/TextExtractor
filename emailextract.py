import re 
def email_extract(file):
    with open ("records.txt",'r') as file:
        records = file.read()
        email_pattern = r"email: ^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$ "