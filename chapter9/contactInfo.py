import pyperclip, re

text = str(pyperclip.paste())
phone_pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    (\d{3})  # First three digits
    (\s|-|\.)  # Separator
    (\d{4})  # Last four digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # Extension
    )''', re.VERBOSE)

email_pattern = re.compile(r'''(
                        [a-zA-Z0-9.%+-]+    # name
                        @    # at sign 
                        [a-zA-Z0-9.-]+    # domain name
                        (\.[a-zA-Z]{2,4})    # period
                        
                          )''', re.VERBOSE)

matches = []

for group in phone_pattern.findall(text):
    phone_number = '-'.join([group[1], group[3], group[5]])
    if group[6] != '':
        phone_number += ' x' + group[6]
    matches.append(phone_number)

for groups in email_pattern.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails found.')

