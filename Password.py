from string import ascii_lowercase, ascii_uppercase
import random

def custome_mode(): 
    # asking user for length of password and with groups should be include
    while True:
            try:
                length = int(input('enter password length: '))
                break
            except ValueError:
                print('wrong input. print integer number')

    while True:
            lower_inc = input('include lowercase? (y/n): ').strip().lower()
            if lower_inc in ("y", "n"):
                break
            print("error: Input must be 'y' or 'n'!")

    while True:
            upper_inc = input('include uppercase? (y/n): ').strip().lower()
            if upper_inc in ("y", "n"):
                break
            print("error: Input must be 'y' or 'n'!")

    while True:
            number_inc = input('include number? (y/n): ').strip().lower()
            if number_inc in ("y", "n"):
                break
            print("error: Input must be 'y' or 'n'!")

    while True:
            symbol_inc = input('include symble? (y/n): ').strip().lower()
            if symbol_inc in ("y", "n"):
                break
            print("error: Input must be 'y' or 'n'!")

    # add all wanted groups to one list 
    groups = []
    if lower_inc == 'y':
        groups.append(lower_lst)
    if upper_inc == 'y':
        groups.append(upper_lst)
    if number_inc == 'y':
        groups.append(number_lst)
    if symbol_inc == 'y':
        groups.append(symbol_list)

    res = []
    # at least one from each group
    for group in groups:
        res.append(random.choice(group))

    # fill reminded positions
    while len(res) < length:
        group = random.choice(groups)
        res.append(random.choice(group))

    # shuffle and print result
    random.shuffle(res)
    print(f"\nyour password is:\n{''.join(res)}\n")

def default_mode():
    # asking user for length of password
    while True:
            try:
                length = int(input('enter password length: '))
                break
            except ValueError:
                print('wrong input. print integer number')

    groups = [lower_lst, upper_lst, number_lst, symbol_list]

    res = []
    # at least one from each group
    for group in groups:
        res.append(random.choice(group))

    # fill reminded positions
    while len(res) < length:
        group = random.choice(groups)
        res.append(random.choice(group))

    # shuffle and print result
    random.shuffle(res)
    print(f"\nyour password is:\n{''.join(res)}\n")    


lower_lst = [i for i in ascii_lowercase]
upper_lst = [i for i in ascii_uppercase]
number_lst = [str(i) for i in range(10)]
symbol_list = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_"]

print('''Welcome to Password Generator!

1. Generate strong passwords automatically (Default Mode)
2. Let you customize passwords with your choice of characters (Custom Mode)
3. End the Program.''')

while True:
    mode = input('\nchose mode [1-2-3]: ')
    
    if mode == '1':
        default_mode()
    elif mode == '2':
        custome_mode()
    elif mode == '3':
        break
    else:
        print('wrong input')