from random import randint

import prompt


def main():
    print('Welcome to the Brain Games!')
        
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    for i in range(0, 3):
        number = randint(0, 1000000)
        if number % 2 == 0:
            parity = 'yes'
        else:
            parity = 'no'
        
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if parity == user_answer.lower():
            print('Correct')
        else:
            print(f""" '{user_answer}' is wrong answer ;(. Correct answer was '{parity}'.
Let's try again, {name}!""")  # noqa: E501

            return False
    
    print(f'Congratulations, {name}!')
    return True
                  

if __name__ == '__main__':
    main() 


