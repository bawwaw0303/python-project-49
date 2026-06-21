from random import randint

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    number = randint(0, 1000000)
    question = str(number)
    answer = 'yes' if number % 2 == 0 else 'no'
    return question, answer


game_dict = {
    'description': description,
    'generate_round': generate_round
}