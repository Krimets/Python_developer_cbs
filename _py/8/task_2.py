# Завдання 2
# Створіть дві функції, що обчислюють значення певних алгебраїчних виразів. На екрані виведіть таблицю значень цих
# функцій від -5 до 5 з кроком 0.5.

def function(x):
    if x < 0:
        return x * 2
    else:
        return x * 3


def main():
    for i in range(-5, 5):
        y = function(i)
        print('function(', i, ') = ', y, sep='')
        y = function(i + 0.5)
        print('function(', i + 0.5, ') = ', y, sep='')


main()
