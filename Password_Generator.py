from string import ascii_lowercase, ascii_uppercase
import random


lower_lst = [i for i in ascii_lowercase]
upper_lst = [i for i in ascii_uppercase]
number_lst = [str(i) for i in range(10)]
symbol_list = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_"]
total_ls = [*lower_lst]
result = []


while True:
    try:
        pass_len = int(input('Enter password Length: '))
        break
    except ValueError:
        print('Wrong Input. Enter integer number.')

while True:
    choice = input('Include uppercase letters? (y/n): ').lower()
    if choice == 'y':
        total_ls.extend(upper_lst)
        break
    elif choice == 'n':
        break
    else:
        print('Wrong Input. Enter y or n.')

while True:
    choice = input('Include numbers? (y/n): ').lower()
    if choice == 'y':
        total_ls.extend(number_lst)
        break
    elif choice == 'n':
        break
    else:
        print('Wrong Input. Enter y or n.')

while True:
    choice = input('Include special characters? (y/n): ').lower()
    if choice == 'y':
        total_ls.extend(symbol_list)
        break
    elif choice == 'n':
        break
    else:
        print('Wrong Input. Enter y or n.')


random.shuffle(total_ls)
for i in range(pass_len):
    result.append(random.choice(total_ls))
print(f'\n{''.join(result)}')