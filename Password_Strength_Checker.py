import re 

def check_password_strength(password):
    password = password.strip()
    
    strength = 0
    
    if len(password) >= 8:
        strength += 1
    
    if re.search(r'[A-Z]', password):
        strength += 1
    
    if re.search(r'[a-z]', password):
        strength += 1
    
    if re.search(r'[@#$%+=?!\-_]', password):
        strength += 1
    
    return strength


def main():
    password = input('Enter your password: ')
    strength = check_password_strength(password)

    if strength == 0:
        print('Password strength: Very Weak')
    elif strength == 1:
        print('Password strength: Weak')
    elif strength == 2:
        print('Password strength: Medium')
    elif strength == 3:
        print('Password strength: Strong')
    elif strength == 4:
        print('Password strength: Very Strong')
    elif strength >= 5:
        print('Password strength: Excellent')


if __name__ == '__main__':
    main()