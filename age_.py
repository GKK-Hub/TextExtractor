import re

def age_extractor(file):
    with open(file,'r') as file:
        records =file.read()
        age_extractor = r"age": ({a-z})
