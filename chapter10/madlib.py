# open the file
# read the file line by line
# search for the words im looking for
# keep the list of words needed in a list
# prompt the user to add words of each kind based on what it found in the file
# substitute those words in the file
# save the results to the text file
# print the results to the screen

import re

pattern = re.compile(r'(?:ADJECTIVE|NOUN|VERB|ADVERB)')

madlib_file = open('madLib.txt', 'r+', encoding='UTF-8')

contents = madlib_file.read()

found = pattern.finditer(contents)

for match in found:
    type = match.group(0)

    if type == 'ADJECTIVE':
        print('Enter an adjective:')
        new_word = input()
    elif type == 'NOUN':
        print('Enter a noun:')
        new_word = input()
    elif type == 'VERB':
        print('Enter a verb:')
        new_word = input()
    else:
        print('Enter an adverb:')
        new_word = input()




