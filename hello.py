# This program says hello and asks for my name

print('Hello, world!')
print('What is your name?')
my_name = input('>')

print('It is good to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))

flag = 1

while flag  == 1:
    print('What is your age?')

    my_age_string = input('>')

    if (my_age_string.isdigit() == True):
        my_age = int(my_age_string)
        if my_age <= 0:
            print('Invalid age - enter an age above 0')
        else:
            print('You will be ' + str(my_age + 1) + ' in a year.')
            flag = 0
    else:
        print('Invalid age - enter a number')