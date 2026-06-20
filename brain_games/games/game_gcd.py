from math import gcd
from random import randint

description = 'Find the greatest common divisor of given numbers.'


def generate_round():
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)

    question = f'{number_1} {number_2}'
    answer = str(gcd(number_1, number_2))

    return question, answer


game_dict = {
    'description': description,
    'generate_round': generate_round
}











