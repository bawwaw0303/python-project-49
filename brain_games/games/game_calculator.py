from random import choice, randint

description = 'What is the result of the expression?'


def generate_round():
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    symbol_list = ['+', '-', '*']
    symbol = choice(symbol_list)
    
    question = f'{number_1} {symbol} {number_2}'
    
    match symbol:
        case '+':
            answer = str(number_1 + number_2)
        case '-':
            answer = str(number_1 - number_2)
        case '*':
            answer = str(number_1 * number_2)
    
    return question, answer


game_dict = {
    'description': description,
    'generate_round': generate_round
}













