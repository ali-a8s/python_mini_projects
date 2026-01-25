from collections import defaultdict

def count_vowels():
    txt = input('enter your text: ')
    vowels = ['a', 'e', 'i', 'o', 'u']
    count_vowels = defaultdict(int)  
    count = 0

    for chr in txt:
        if chr.lower() in vowels:
            count += 1
            count_vowels[chr.lower()] += 1  

    print(f'the number of vowels is {count}')
    print(dict(count_vowels)) 


print("\nCOUNT VOWELS\n")

def main():
    while True:
        choice = input('run program? [y/n] ')
        if choice.lower() == 'y':
            count_vowels()
        elif choice.lower() == 'n':
            break
        else:
            print('wrong input')


if __name__ == '__main__':
    main()