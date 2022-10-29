print([1, 2, 3, 4, 5][1: 125])
print([1, 2, 3, 4, 5][1:3])

print('ABC' < 'ABC')
print([1, 2, 3] < [1, 2, 4])

a, b, c = 1, 2, 3
# міняємо місцями значення двох змінних:
my_tuple = 10, 50, 90
a, b = b, a
a, b, c = my_tuple
print(a, b, c)