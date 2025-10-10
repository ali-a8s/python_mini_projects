import random 
import time


print('welcome to rock paper scissor game.')

user_point = 0
computer_point = 0

shapes = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']



def game(user_point, computer_point):
    user = input('enter your choice (Type 0 for Rock, 1 for Paper or 2 for Scissors)\n0/1/2: ')
    computer = random.randint(0, 2)

    if (not user.isdigit()) or (user not in ['0', '1', '2']):
        print('invalid input')
        return user_point, computer_point

    user = int(user)

    print("\nRock...")
    time.sleep(0.5)
    print("Paper...")
    time.sleep(0.5)
    print("Scissors...")
    time.sleep(0.5)
    print("Shoot!\n")
    time.sleep(0.3)

    print(f'\nyour choice:\n{shapes[user]}')
    print(f'computer choice:\n{shapes[computer]}')

    if computer == user:
        print("it's a DRAW")
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        print('you WIN')
        user_point += 1
    else:
        print('you LOSE')
        computer_point += 1

    print(f'your points: {user_point} | computer points: {computer_point}')
    return user_point, computer_point



while True:
    choice = input('\ndo you wanna play? (y/n) ')
    
    if choice.lower() == 'y':
        user_point, computer_point = game(user_point, computer_point)
    elif choice.lower() == 'n':
        print(f'Final Score → You: {user_point} | Computer: {computer_point}')
        break
    else:
        print('wrong input')
