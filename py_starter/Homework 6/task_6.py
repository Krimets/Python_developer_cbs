# Завдання 6
# Для цього завдання вихідний список значень беремо з підсумкового списку new_list додаткового завдання 2.
# Користувач вводить з клавіатури значення; якщо таке є у цьому списку — вивести кількість його повторів
# та його позицію у цьому списку.

from task_5 import new_list

positions = []
p = 'None'
y = input('Введіть значення: ')

if y in new_list:
    counter = new_list.count(y)
    print(f'В списку знайдено {counter} повторів значення {y}')
    while y in new_list:
        p = new_list.index(y)
        positions.append(p)
        new_list.insert(p, None)
        new_list.remove(y)
    print(f'Значення знайдено на такіх позиціях: {positions}')
else:
    print('Значення відсутнє')
