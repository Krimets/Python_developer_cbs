# Завдання 1
# Дано два рядки. Виведіть на екран символи, які є в обох рядках.

s3 = []
s1 = input('Введіть перший рядок: ')
s2 = input('Введіть другий рядок: ')

while s1:
    for i in s1:
        if i in s2 and i not in s3:
            s3.append(i)
        else:
            s1 = s1[1:]
print(s3)
