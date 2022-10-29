# Завдання 2
# Створіть програму, яка перевіряє, чи є паліндромом введена фраза.

def inspect(a):
    a = a.replace(' ', '')
    if a.upper() == a[::-1].upper():
        print('Фраза є паліндромом')
    else:
        print('Фраза не є паліндромом')


def request():
    inspect(input('Введіть фразу: '))


request()
