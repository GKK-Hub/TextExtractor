import re

def age_extract(file):
    with open("records.txt","r") as file:
        records=file.read()
        age_pattern=r"Age:({/d})"