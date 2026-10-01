import re
def names_etr(file):
    with open(file, "r") as file:
        records = file.read()
        name_pattern= r"Name: ()"