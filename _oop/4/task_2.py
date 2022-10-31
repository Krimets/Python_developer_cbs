# Завдання 2
# Напишіть програму-калькулятор, яка підтримує такі операції: додавання, віднімання, множення, ділення та піднесення
# до ступеня. Програма має видавати повідомлення про помилку та продовжувати роботу під час введення некоректних
# даних, діленні на нуль та зведенні нуля в негативний степінь.

from math import pow


def dan():
    return float(input('Введiть перше число: ')), float(input('Введiть друге число: '))


def one_c():
    return float(input('Введiть число: '))


def my_sum():
    x, y = dan()
    return 'Результат =', x + y


def minus():
    x, y = dan()
    return 'Результат =', x - y


def mn():
    x, y = dan()
    return 'Результат =', x * y


def dil():
    x, y = dan()
    try:
        return 'Результат =', x / y
    except Exception as ex:
        return 'Не можна ділити на 0', ex


def stu():
    x, y = dan()
    try:
        return 'Результат =', pow(x, y)
    except Exception as ex:
        return 'Помилка при зведенні нуля в негативний степінь', ex


def action():
    try:
        d = int(input('''
Оберiть дiю (число):
1. Додавання
2. Віднімання
3. Множення
4. Ділення
5. Зведення в ступінь
6. Вийти
= '''))
        if d == 1:  # 1. Додавання
            print(*my_sum())
            action()
        elif d == 2:  # 2. Віднімання
            print(*minus())
            action()
        elif d == 3:  # 3. Множення
            print(*mn())
            action()
        elif d == 4:  # 4. Ділення
            print(*dil())
            action()
        elif d == 5:  # 5. Зведення в ступінь
            print(*stu())
            action()
        elif d == 6:  # 6. Вийти
            print('Завершення програми')
        else:
            print('Потрiбно обрати дiю (1-6), спробуйте ще раз')
            action()
    except Exception as e:
        print(f'Помилка вводу "{e}", почнiть з початку')
        action()


action()
