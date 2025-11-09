import random, sys

def play(user_choice, computer_choice, wins, losses, ties):
    
    match computer_choice:
            case 1:
                print('ROCK')
                match user_choice:
                    case 'r':
                        print('It is a tie!')
                        ties += 1
                    case 'p':
                        print('You win!')
                        wins += 1
                    case 's':
                        print('You lose!')
                        losses += 1
            case 2:
                print('PAPER')
                match user_choice:
                    case 'r':
                        print('You lose!')
                        losses += 1
                    case 'p':
                        print('It is a tie!')
                        ties += 1
                    case 's':
                        print('You win!')
                        wins += 1
            case 3:
                print('SCISSORS')
                match user_choice:
                    case 'r':
                        print('You win!')
                        wins += 1
                    case 'p':
                        print('You lose!')
                        losses += 1
                    case 's':
                        print('It is a tie!')
                        ties += 1
    return wins, losses, ties

def main():
    wins = 0
    losses = 0
    ties = 0

    print('ROCK, PAPER, SCISSORS')

    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        user_choice = input('>')
        match user_choice:
            case 'r':
                print('ROCK versus...')
            case 'p':
                print('PAPER versus...')
            case 's':
                print('SCISSORS versus...')
            case 'q':
                sys.exit()
            case _:
                print('Invalid entry - try again')
                continue
        
        computer_choice = random.randint(1,3)
        wins, losses, ties = play(user_choice, computer_choice, wins, losses, ties)
    

        print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')

if __name__ == "__main__":
    main()
    

