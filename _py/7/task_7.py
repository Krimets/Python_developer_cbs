# Завдання 7
# Створіть прототип програми «Бібліотека», в якій є можливість перегляду та внесення змін до структури:
# прізвище:
# посада: ...
# досвід роботи: …
# портфоліо: …
# коефіцієнт ефективності: …
# стек технологій: …
# зарплата: …
# Передбачте можливість виведення на екран сортування за прізвищем та найефективнішим співробітником.

import operator


d = dict()


def inp():
    b = input('''
Вітаю у віртуальній бібліотеці
Внести зміни = Натисніть 1
Переглянути всі данні = Натисніть 2
Сортувати за прізвищем = Натисніть 3
Сортувати за ефективностю = Натисніть 4
Для виходу = Натисніть 5
>>> ''')
    return b


def library():
    b = inp()
    if b == '1':
        surname = input('''Введіть прізвище (q - завершити):
>>> ''')
        if surname == 'q':
            library()
        else:
            d.setdefault(surname, {'посада': None, 'досвід роботи': None})
        position = input('''Введіть посаду:
>>> ''')
        experience = input('''Введіть досвід роботи:
>>> ''')
        portfolio = input('''Введіть портфоліо:
>>> ''')
        efficiency = float(input('''Введіть коефіцієнт ефективності:
>>> '''))
        technology_stack = input('''Введіть стек технологій:
>>> ''')
        salary = input('''Введіть зарплатню:
>>> ''')
        d[surname] = {'посада': position, 'досвід роботи': experience, 'портфоліо': portfolio,
                      'коефіцієнт ефективності': efficiency, 'стек технологій': technology_stack, 'зарплатня': salary}
        print('Зміни внесені')
        library()

    elif b == '2':
        if d == {}:
            print('Нічого не знайдено')
            library()
        else:
            for surname in d:
                print(surname, '-', d[surname])
            library()

    elif b == '3':
        if d == {}:
            print('Нічого не знайдено')
            library()
        else:
            sorted_d = sorted(d.items())
            for i in sorted_d:
                print(*i, end='\n')
            library()

    elif b == '4':
        if d == {}:
            print('Нічого не знайдено')
            library()
        else:
            r = {}
            for i in d:
                get = operator.itemgetter('коефіцієнт ефективності')
                g = get(d[i])
                r[g] = i
            sorted_r = sorted(r.items())
            sorted_r.sort(reverse=True)
            print('Ефективність:')
            for i in sorted_r:
                print(*i, end='\n')
            library()

    elif b == '5':
        print('Допобачення')
    else:
        print('Помилка, почніть спочатку')
        library()


library()
