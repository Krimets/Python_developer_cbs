# Завдання 3
# Використовуючи вкладені цикли та функції print(‘*’, end=’’), print(‘ ‘, end=’’) та print() виведіть
# на екран прямокутний трикутник

for i in range(10):
    print(' ', end='')
    for y in range(1, i):
        print('*', end='')
    print()
