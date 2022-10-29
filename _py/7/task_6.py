# Завдання 6
# Створіть прототип програми «Бібліотека», де є можливість перегляду та внесення змін за структурою: автор: твір.
# Передбачте можливість виведення на екран сортування за автором та твором.

d = dict()


def inp():
    b = input('''
Вітаю у віртуальній бібліотеці
Бажаєте внести зміни = Натисніть 1
Переглянути всі твори = Натисніть 2
Сортувати за автором = Натисніть 3
Сортувати за твором = Натисніть 4
Для виходу = Натисніть 5
>>> ''')
    return b


def library():
    b = inp()
    if b == '1':
        author = input('''Введіть автора (q - завершити):
>>> ''')
        if author == 'q':
            library()
        book = input('''Введіть назву твору (q - завершити):
>>> ''')
        if book == 'q':
            library()
        else:
            d[book] = author
            print('Зміни внесені')
            library()
    elif b == '2':
        if d == {}:
            print('Нічого не знайдено')
            library()
        else:
            for book in d:
                print(book, '-', d[book])
            library()
    elif b == '3':
        if d == {}:
            print('Нічого не знайдено')
            library()
        else:
            for book in d:
                print(d[book], '-', book)
            library()
    elif b == '4':
        if d == {}:
            print('Нічого не знайдено')
            library()
        else:
            sorted_d = sorted(d.items())
            for i in sorted_d:
                print(*i, end='\n')
            library()
    elif b == '5':
        print('Допобачення')
    else:
        print('Помилка, почніть спочатку')
        library()


library()
