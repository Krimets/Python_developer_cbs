# Завдання 1
# Напишіть скрипт, який створює текстовий файл і записує до нього 10000 випадкових дійсних чисел.
# Створіть ще один скрипт, який читає числа з файлу та виводить на екран їхню суму.

from random import choice

counter = 0
random_sum = 0

with open('10000.txt', 'w') as file:
    while counter < 10000:
        file.write(str(choice(range(-10000, 10000))) + ',')
        counter += 1

with open('10000.txt', 'r') as file:
    txt = file.read().split(',')
for _ in txt:
    if _:
        random_sum += int(_)
print('Сума чисел файлу:', random_sum)
