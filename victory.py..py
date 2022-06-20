while True:

    right_answer = 0
    wrong_answer = 0
    import random
    numbers = ['pushkin', 'mozart', 'picasso', 'mikilanjilo', 'magellan', 'repin', 'einstein', 'newton']

    result = random.sample(numbers, 5)
    print(result)



    answer_dict = {
        'picasso': '25.10.1881',
        'repin': '05.08.1844',
        'magellan': '20.10.1480',
        'einstein': '18.04.1955',
        'newton': '04.01.1643',
        'mozart': '27.01.1756',
        'pushkin': '06.05.1799',
        'mikilanjilo': '27.01.1756',
    }


    for name in result:
        data = input(f'Введите дату рождения для {name} в формате dd.mm.yyyy: ')
        if data == answer_dict[name]:
            right_answer += 1
        else:
            wrong_answer += 1
    print('Правильно:', right_answer)
    print('Не правильно:', wrong_answer)

    resume_victory = (input('Продолжим игру: '))
    if resume_victory == 'нет':
        break
print('GameOver')








































