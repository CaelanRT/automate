import re

def strip(string, char=''):
    # if 2nd arg == '', then we group the input string with everything and spaces and then just return the string
    # else, we regex that character and remove it from the entire string
    if char == '':
        string_pattern = re.compile(r'''(
                                   (\s)?    # preceding spaces
                                   (\w)     # string
                                   (\s)?    # spaces at the end
                                   )
                                ''', re.VERBOSE)
        print(string_pattern.findall(string))

strip('   hello   ')