def addition():
    try:
        nums = list(map(int, input('enter all numbers separated by space: ').split()))
        print(f'answer = {sum(nums)}')
    except ValueError:
        print('wrong input')

def subtraction():
    try:
        num_1 = int(input('enter first number: '))
        num_2 = int(input('enter second number: '))
        print(f'answer = {num_1 - num_2}')
    except ValueError:
        print('wrong input')

def multiplication():
    try:
        nums = list(map(int, input('enter all numbers separated by space: ').split()))
        result = 1
        for num in nums:
            result *= num
        print(f'answer = {result}')
    except ValueError:
        print('wrong input')

def division():
    try:
        num_1 = int(input('enter first number: '))
        num_2 = int(input('enter second number: '))
        print(f'answer = {num_1 / num_2}')
    except ZeroDivisionError:
        print('second number cant be zero')
    except ValueError:
        print('wrong input')

def average():
    try:
        nums = list(map(int, input('enter all numbers separated by space: ').split()))
        result = sum(nums) / len(nums)
        print(f'answer = {result}')
    except ValueError:
        print('wrong input')

def power():
    try: 
        base = int(input('enter base: '))
        exp = int(input('enter exponent: '))
        print(f'answer = {base ** exp}')
    except ValueError:
        print('wrong input')




print(menue := '''-1 for menue.
0 to exit.
1 for addition.
2 for subtraction.
3 for multiplication.
4 for division.
5 for average.
6 for power.''')


while True:
    choice = input('\nenter your choice: ')

    try:
        choice = int(choice)
    except ValueError:
        print('input must be integer number.')
        continue

    if choice == -1:
        print(menue)
    elif choice == 0:
        break
    elif choice == 1:
        addition()
    elif choice == 2:
        subtraction()
    elif choice == 3:
        multiplication()
    elif choice == 4:
        division()
    elif choice == 5:
        average()
    elif choice == 6:
        power()
    else:
        continue


