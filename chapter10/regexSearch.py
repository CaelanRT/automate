# create a regex for .txt
# get a user supplied regex 
# use that regex to search for all files that match in the path
# open each file and check if the regex from the user matches anything in the files
# print the results if found

import re
from pathlib import Path

# content = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."

def find_regex(content):
    found_list = user_regex.findall(content)
    joined_list = ",\n".join(found_list)
    print(joined_list)

# loop + printing to create regex and search contents of a file
while True:
    
    print("Enter your regex:")
    user_input = input()

    try:
        user_regex = re.compile(user_input)
        break
    except:
        print("Invalid regex.")

# loop to search for files
for name in Path('.').glob('*.txt'):
    txt_file = open(name, 'r', encoding="UTF-8")
    content = txt_file.read()
    find_regex(content)
    txt_file.close()







