# Завдання 5
# Є рядок, в якому зберігаються 1000 слів. Створіть словник із ключами - унікальними словами та значеннями - кількістю
# повторів кожного слова у послідовності.

r = 'python C++ task Task Homework HomeWork HomewOrk, py,PY,Py;cbs;CBS'
r = r.replace('. ', ' ').replace(', ', ' ').replace(',', ' ').replace('.', ' ').replace(';', ' ').replace(':', ' ')
r = r.split(' ')
r2 = []
s = dict()
for i in r:
    r2.append(i.upper())
for i in r2:
    counter = r2.count(i)
    if i not in s:
        s[i] = counter
print(s)
