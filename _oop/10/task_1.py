# Завдання 1
# Написати функцію, яка за допомогою регулярних виразів розбиває текст на окремі слова і знаходить частоту окремих слів.

from re import split, compile

a = 'Написати виразів виразів функцію знаходить яка за допомогою регулярних виразів текст розбиває текст на окремі ' \
    'слова знаходить частоту окремих слів допомогою виразів'
s = []


def reg(string):
    result = split(r'\s', string)
    print(result)
    return result


def res(lis, string):
    for i in lis:
        pattern = compile(i)
        result = pattern.findall(string)
        result1 = f'Слово: "{result[0]}", Частота = {len(result)}\n'
        if result1 not in s:
            s.append(result1)
    return [y for y in s]


print('\n', *res(reg(a), a))
