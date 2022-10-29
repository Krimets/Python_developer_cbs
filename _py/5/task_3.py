# Завдання 3
# Напишіть програму, яка на вхід отримує параметри кольору (в діапазоні від 0 до 255 для кожного кольору)
# у форматі RGB і виводить на екран кортеж, у якому зберігається колір.

from collections import namedtuple

t = False
rgb = namedtuple('RGB', 'R G B')
RGB = rgb(int(input()), int(input()), int(input()))
for i in RGB:
    if 0 < i < 256:
        t = True
    else:
        print('Помилка, треба в діапазоні від 0 до 255 для кожного кольору')
        break
if t:
    print(RGB)
