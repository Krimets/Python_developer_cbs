# Завдання 2
# Відкрийте файл fix_me.py із папки homework. Використовуючи звичайний текстовий редактор (Notepad), виправте
# всі помилки оформлення коду згідно з PEP 8.

from math import pi
from math import e

p = 5
counter = int(input('Введите количество повторов: '))
print(p * counter)
print(pi * p * counter)
print(e * 2)

while p >= 0:
    p -= 1
s = 'my string'
su = 0

for elem in s:
    su += pow(s.find(elem), 2)
    print("sum =", su)


def my_func(atr=1):
    return 'atr', atr


print(my_func(5))
