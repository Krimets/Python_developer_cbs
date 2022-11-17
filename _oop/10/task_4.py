# Завдання 4
# Напишіть функцію, яка буде аналізувати текст, що надходить до неї, і виводити тільки унікальні слова на екран,
# загальну кількість слів і кількість унікальних слів.

from re import compile

a = 'Написати виразів виразів функцію знаходить яка за допомогою регулярних виразів текст розбиває текст на окремі ' \
    'слова знаходить частоту окремих слів допомогою виразів'
s = []


def res(string):
    counter = 0
    uni_counter = 0
    for i in string.split():
        pattern = compile(i)
        counter += 1
        result = pattern.findall(string)
        if len(result) < 2:
            uni_counter += 1
            s.append(result[0])
    return f"Унікальні слова: {s}\nЗагальна кількість слів: {counter}\nКількість унікальних слів: {uni_counter}"


print(res(a))
