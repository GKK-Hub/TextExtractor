import re

def pan_extract(file):
    with open ('records.txt', 'r') as f:
        data = f.read()
        pan_numbers = re.findall(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b', data)
        return pan_numbers

    print (pan_extract('records.txt'))