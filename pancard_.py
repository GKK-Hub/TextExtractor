import re 

def pan_extractor(file):
    pan_pattern = r'\b[A-Z]{5}[0-9]{4}[A-Z]\b'
    pan_numbers = []

    with open(file, 'r') as f:
        content = f.read()
        pan_numbers = re.findall(pan_pattern, content)

    return pan_numbers

print (pan_extractor('records.txt'))