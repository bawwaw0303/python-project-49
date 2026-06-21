import math
from random import randint

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Функция проверки числа на простое"""
    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number)) 
    divisors = range(2, (number_sqrt + 1))
    for element in divisors:
        if number % element == 0:
            return False
    return True


def generate_round():
    n = randint(0, 1000)
    question = str(n)

    if is_prime(n):
        answer = 'yes'
    else:
        answer = 'no'
    
    return question, answer


game_dict = {
    'description': description,
    'generate_round': generate_round
}
