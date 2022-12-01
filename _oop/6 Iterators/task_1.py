# Завдання 1
# Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable

iterable = range(1, 101)

iter_obj = iter(iterable)

while True:
    try:
        element = next(iter_obj)
        print(element, end='')
    except StopIteration:
        print(' <<< end')
        break
