n = 0
m = 1
x = 0

while x < 10:
    t = int(input('Введiть значення: '))
    n += t
    m *= t
    x += 1

print('Сума: ', n, ' Добуток: ', m)
