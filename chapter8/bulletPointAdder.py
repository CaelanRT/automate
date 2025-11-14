import pyperclip

text = pyperclip.paste()

textList = text.splitlines()

addition = '* '

for i in range(len(textList)):
    textList[i] = addition + textList[i]

newText = '\n'.join(textList)
    
pyperclip.copy(newText)