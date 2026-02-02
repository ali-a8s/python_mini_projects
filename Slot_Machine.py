import random 


def get_balance():
    while True:
        try:
            balance = int(input('enter your starting balance: $'))
            if balance <= 0:
                print('Balance must be a positive number.')
            else:
                return balance
        except ValueError:
            print('Please enter a valid number')


def get_bet(balance):
    while True:
            try:
                bet = int(input('Enter your bet amount: $'))
                if (bet > balance) or (bet <= 0):
                    print(f'Invalid bet amount. You can bet between $1 and ${balance}')
                else:
                    return bet
            except ValueError:
                print('Please enter a valid number for the bet amount.')


def spin_reels():
    symbols = ['@', '#', '$', '%', '&']
    return [random.choice(symbols) for _ in range(3)]


def display_reels(reels):
    print(f"{reels[0]} | {reels[1]} | {reels[2]}")


def calculate_payout(reels, bet):
    if (reels[0] == reels[1]) and (reels[0] == reels[2]):
        return bet * 10
    if (reels[0] == reels[1]) or (reels[0] == reels[2]) or (reels[1] == reels[2]):
        return bet * 2
    return 0
     

def main():
    balance = get_balance()
    
    print('\nwelcome to the Slot Machine!')
    print(f'you start with a balance of ${balance}\n')

    while balance > 0:
        print(f'Current balance: ${balance}')
        
        bet = get_bet(balance)
        reels = spin_reels()
        display_reels(reels)
        payaout = calculate_payout(reels, bet)

        if payaout > 0:
            print(f'You won ${payaout}!')
        else:
            print('You lost!')
        
        balance += payaout - bet
        if balance <= 0:
            print('You are out of money. Game Over')
            break

        play_again = input('\ndo u wanna play again? (y/n): ').lower()
        if play_again != 'y':
            print(f'you walk away with ${balance}.')
            break


if __name__=='__main__':
    main()