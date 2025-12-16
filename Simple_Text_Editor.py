import os

def main():
    filename = input('enter the filename to open or create: ').strip()
    
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                content = file.read()
                print(content)
        else:
            with open(filename, 'w') as file:
                pass
    except OSError:
        print(f'{filename} could not be opened.')
        return 

    print('\nEnter your text (type SAVE in a new line to save and exist)')
    content = []
    while True:
        line = input()
        if line == 'SAVE':
            break
        content.append(line)
    
    try:
        with open(filename, 'w') as file:
            file.write('\n'.join(content))
            print(f'\n{filename} saved.')
    except OSError:
        print(f'{filename} could not be saved')

if __name__ == '__main__':
    main()