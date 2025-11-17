import re

def strongPass(password):
    length_regex = re.compile(r'.{8,}')
    
    if length_regex.search(password) == None:
        return False
    
    uppercase_regex = re.compile(r'[A-Z]')

    if uppercase_regex.search(password) == None:
        return False
    
    lowercase_regex = re.compile(r'[a-z]')

    if lowercase_regex.search(password) == None:
        return False
    
    number_regex = re.compile(r'[0-9]')

    if number_regex.search(password) == None:
        return False

    return True

print(strongPass('ASdf12345!'))