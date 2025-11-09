my_pets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter pet name: ')
name = input()
if name not in my_pets:
    print('I do not have a pet name ' + name)
else:
    print(name + ' is my pet.')