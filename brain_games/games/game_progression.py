from random import randint

description = 'What number is missing in the progression?'


def generate_progression():
    """Функция для генерации прогрессии"""
    start_progression_number = randint(0, 10)
    step_of_progression = randint(1, 5)
    length_of_progression = randint(5, 10)

    progression_list = [start_progression_number]
    for i in range(1, length_of_progression):
        next_number = progression_list[i - 1] + step_of_progression
        progression_list.append(next_number)

    return progression_list


def generate_round():
    progression = generate_progression()
    random_index = randint(0, len(progression) - 1)

    answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(map(str, progression))

    return question, str(answer)


game_dict = {
    'description': description,
    'generate_round': generate_round
}
