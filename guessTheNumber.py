import random, sys


print('I am thinking of a number between 1 and 20.')

rand_number = random.randint(1,20)
num_guesses = 0

while True:
    print('Take a guess')
    guess = int(input('>'))


    if (guess > rand_number):
        print('Guess is too high.')
        num_guesses += 1
    elif(guess < rand_number):
        print('Guess is too low')
        num_guesses += 1
    else:
        print('Good job! You got it in ' + str(num_guesses) + ' guesses!')
        sys.exit()

    