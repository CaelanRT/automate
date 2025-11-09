def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number, end = ' ')
        return number
    else:
        number = 3 * number + 1
        print(number, end = ' ')
        return number
    
def main():
    print('Enter number:')

    while True:
        try:
            number = int(input('>'))
            break
        except:
            print('Invalid entry - please enter a number')

    while number != 1:
        number = collatz(number)
    print()

if __name__ == '__main__':
    main()
