# Завдання 5
# Створіть список натуральних чисел int_list. Кожне непарне значення списку додайте до нового списку new_list.
# Користувач вводить з клавіатури кількість повторів списку repeat. Здійсніть дублювання списку new_list, repeat
# кількість разів. Очистіть список int_list.

int_list = list(input('Створіть список натуральних чисел: '))
new_list = []
for i in int_list:
    if int(i) % 2 != 0:
        new_list.append(i)

repeat = int(input('Введіть кількість повторів: '))
new_list *= repeat
print(new_list)

int_list.clear()
print(int_list)
