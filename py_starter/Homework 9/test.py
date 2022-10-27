def summa(i, n):
    if n == i:
        return i
    else:
        return n + summa(i, n - 1)


num = int(input('''Введіть початок
>>> '''))
num2 = int(input('''Введіть кінець
>>> '''))
print("Сума чисел проміжку:", summa(num, num2))
