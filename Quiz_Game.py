import random
from termcolor import cprint


def ask_question(index, question, options):
    print(f'\nQuestion {index}:  {question}') 
    for option in options:
        print(option)
    
    return input('Your answer: ').upper().strip()


def run_quiz(questions):
    random.shuffle(questions)

    score = 0

    for index, item in enumerate(questions, 1):
        answer = ask_question(index, item['question'], item['options'])

        if answer == item['answer']:
            cprint('Correct', 'green')
            score += 1
        else:
            cprint(f'Wrong. the correct answer is {item['answer']}', 'red')

    print(f'\nQuiz over. your final score is {score} out of {len(questions)}')


def main():
    questions = [
        {
            'question': '2 + 2 ?',
            'options': ['A. 5', 'B. 9', 'C. 4', 'D. 3'],
            'answer': 'C'
        },
        {
            'question': '4 * 5 ?',
            'options': ['A. 20', 'B. 35', 'C. 40', 'D. 15'],
            'answer': 'A'
        },
        {
            'question': '10 - 3 ?',
            'options': ['A. 8', 'B. 9', 'C. 6', 'D. 7'],
            'answer': 'D'
        }
    ]
    run_quiz(questions)

if __name__ == '__main__':
    main()