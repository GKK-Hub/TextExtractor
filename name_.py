import re

def name_extract(file):
    with open(file, 'r') as file:
        records = file.read()  # str object
        name_pattern = r"Name: ({a-z}\b)"
        names = re.findall(pattern=name_pattern,
                           string=records)
    return names

print(name_extract('records.txt'))