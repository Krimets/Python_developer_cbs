# Завдання 2
# Модифікуйте вихідний код сервісу зі скорочення посилань з ДЗ 7 заняття курсу Python Starter так,
# щоб він зберігав базу посилань на диску і не «забув» при перезапуску. За бажанням можете ознайомитися з модулем
# shelve (https://docs.python.org/3/library/shelve.html), який у даному випадку буде дуже зручним та спростить
# виконання завдання.

import shelve


def get_key(sh, value):
    for k, v in sh.items():
        if v == value:
            return k


v = input('Введіть посилання: ')
k = input('Введіть назву: ')
shelf = shelve.open('mydata')
shelf[k] = v
print('Додано!')
shelf.close()
t = True

while t:
    r = input('''
    Хочете отримати початкове посилання? --> Напишіть коротку назву
    Хочете отримати коротку назву? --> Введіть повне посилання
    Додати посилання та назву? --> Введіть 'y'
    Для виходу натисніть будь що.
    >>>''')
    shelf = shelve.open('mydata')
    key = get_key(shelf, r)
    if key:
        print('Коротка назва:', key)
        shelf.close()
    elif r in shelf:
        print('Початкове посилання:', shelf[r])
        shelf.close()
    elif r.lower() == 'y':
        v = input('Введіть посилання: ')
        k = input('Введіть назву: ')
        shelf[k] = v
        shelf.close()
        print('Додано!')
    else:
        print('Допобачення')
        t = False
