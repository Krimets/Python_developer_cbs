# Завдання 3
# Створіть модуль для отримання простих чисел. Імпортуйте його з іншого модуля. Імпортуйте його окремі імена.


lst = []
a = int(input('Задайте початок промiжку: '))
b = int(input('Тепер кiнець промiжку: '))


def prime(a, b):
    for i in range(a, b+1):
        counter = 0
        for y in range(1, i+1):
            if i % y == 0:
                counter += 1
        if counter == 2:
            lst.append(i)
    return 'Всі прості числа проміжку:', lst


print(*prime(a, b))
