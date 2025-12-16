def print_menu():
    print('\n1. View Tasks')
    print('2. Add a Task')
    print('3. Remove a Task')
    print('4. Exit')

def get_choice():
    while True:
        choice = input('Enter your choice: ')
        valid_choices = ('1', '2', '3', '4')
        if choice not in valid_choices:
            print('Invalid Input')
            continue
        else:
            return choice 

def view_tasks(lst):  
    if not lst:
        print('No tasks in the list')
    else:
        for index, item in enumerate(lst):
            print(f'{index+1}. {item}')

def add_task(lst): 
    task = input('Enter a new task: ')
    lst.append(task)

def delete_task(lst):
    if not lst: 
        print('No tasks to delete')
        return
    
    view_tasks(lst)  

    while True:
        try: 
            task_number = int(input('Enter task number: '))
            if 1 <= task_number <= len(lst):
                lst.pop(task_number-1)
                print(f'Task {task_number} removed successfully!')
                break
            else: 
                print('Invalid task number')
        except ValueError:
            print('Please enter a valid number')



def main():
    todos = []

    while True:
        print_menu()

        choice = get_choice()

        if choice == '1':  
            view_tasks(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            delete_task(todos)
        elif choice == '4':
            print('Goodbye!')
            break


if __name__ == '__main__':
    main()