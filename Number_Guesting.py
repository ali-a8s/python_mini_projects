import random


def clear_screen():
    print('\n' * 100)

def game():
    while True:
        try:
            low = int(input('min value: '))
            break
        except ValueError:
            print('wrong input. print number')

    while True:
        try:
            high = int(input('max value: '))
            break
        except ValueError:
            print('wrong input. print number')

    if low > high:
        print('low was greater then high. so i switch them.')
        low, high = high, low

    while True:
        try:
            level = int(input('difficulty level (1 for easy [10 chances] -- 2 for hard [5 chances]): '))
            if level == 1:
                count = 10
                break
            elif level == 2:
                count = 5
                break
            else:
                print('wrong input. i set it on easy')
                count = 10
                break
        except ValueError:
            print('input must be 1 or 2. try again')

    answer = random.randint(low, high)

    print(f'\nyou have {count} chances to geuss the number between {low} - {high}')

    while True: 
        guess = int(input('\nEnter your guess: '))

        if guess > answer:
            print('go DOWN')
            count -= 1
            print(f'chances left {count}')
        elif guess < answer:
            print('go UP')
            count -= 1
            print(f'chances left {count}')
        elif guess == answer:
            print(f'you WIN.\npoint = {count}')
            break
        
        if count == 0:
            print(f'you LOST, the answer was {answer}')
            break



print('Welcome to number guesing game')
while True:
    play = input('do you wanna play [y/n]: ')
    if play.lower() == 'y':
        clear_screen()
        game()
    elif play.lower() == 'n':
        break
    else:
        print('wrong input. try again\n')