import prompt


def game_engine(game):
    """Запуск игры с общей логикой"""
    round_for_wins = 3

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    game_description = game.get('description', 'description not found')
    print(game_description)
    
    for _ in range(round_for_wins):
        question, result = game['generate_round']()
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if user_answer == result:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{result}'.\n"
                f"Let's try again, {name}!"
                )
            
            return False
        
    print(f'Congratulations, {name}!')
    return True



    
    














