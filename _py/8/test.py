import math


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


def dil():
    x, y = dan()
    if y == 0:
        return 'Значення != 0 !'
    return 'Результат =', x / y


def stu():
    x, y = dan()
    return 'Результат =', pow(x, y)


def qva():
    x = one_c()
    return 'Результат =', math.sqrt(x)


def cube():
    x = one_c()
    return 'Результат =', x ** (1 / 3)


def sinn():
    x = one_c()
    return 'Результат =', math.sin(x)


def coss():
    x = one_c()
    return 'Результат =', math.cos(x)


def tang():
    x = one_c()
    return 'Результат =', math.tan(x)


def mn():
    x, y = dan()
    return 'Результат =', x * y


def action():
    try:
        d = int(input('''Вiтаю, оберiть дiю (число):
1. Додавання
2. Віднімання
3. Множення
4. Ділення
5. Зведення в ступінь
6. Квадратний корінь
7. Кубічний корінь
8. Знайти синус
9. Знайти косинус
10. Знайти тангенс
= '''))
        if d == 1:  # 1. Додавання
            print(*my_sum())
        elif d == 2:  # 2. Віднімання
            print(*minus())
        elif d == 3:  # 3. Множення
            print(*mn())
        elif d == 4:  # 4. Ділення
            print(*dil())
        elif d == 5:  # 5. Зведення в ступінь
            print(*stu())
        elif d == 6:  # 6. Квадратний корінь
            print(*qva())
        elif d == 7:  # 7. Кубічний корінь
            print(*cube())
        elif d == 8:  # 8. Знайти синус
            print(*sinn())
        elif d == 9:  # 9. Знайти косинус
            print(*coss())
        elif d == 10:  # 10. Знайти тангенс
            print(*tang())
        else:
            print('Потрiбно обрати дiю (1-10), спробуйте ще раз')
            action()
    except:
        print('Помилка вводу, почнiть з початку')
        action()


action()
print('Завершення програми')
