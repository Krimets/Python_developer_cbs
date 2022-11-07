# Завдання 3
# Напишіть функцію-генератор для отримання n перших простих чисел.

b = int(input('Скільки перших простих чисел бажаєте отримати?\n>>> '))


def gen(b):
    for i in range(0, b * 100):
        counter = 0
        for y in range(1, i+1):
            if i % y == 0:
                counter += 1
        if counter == 2:
            yield i


g = gen(b)
print(f'{b} перших простих чисел: ')
prime_counter = 1
while prime_counter < b + 1:
    try:
        print(f'{prime_counter}. {next(g)}')
    except StopIteration:
        break
    prime_counter += 1
