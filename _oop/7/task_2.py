# Завдання 2
# Виведіть із списку чисел список квадратів парних чисел. Використовуйте 2 варіанти рішення: генератор та цикл

s = [4, 5, 6, 7, 8, 9, 10]


def gen(s):
    for _ in s:
        if _ % 2 == 0:
            yield _ ** 2


g = gen(s)
while True:
    try:
        print(next(g), end=' ')
    except StopIteration:
        break
