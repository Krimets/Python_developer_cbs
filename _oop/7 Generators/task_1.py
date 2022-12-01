# Завдання 1
# Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).

s = [4, 5, 6, 7, 8, 9, 10]


def gen(s, i):
    for _ in s:
        yield s[i]
        i -= 1


g = gen(s, -1)
while True:
    try:
        print(next(g), end=' ')
    except StopIteration:
        break
