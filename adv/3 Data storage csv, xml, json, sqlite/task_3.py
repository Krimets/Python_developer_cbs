# Завдання 3
# Попрацюйте зі створенням власних діалектів, довільно вибираючи правила для CSV-файлів. Зареєструйте створені
# діалекти та попрацюйте, використовуючи їх зі створенням/читанням файлом.

import csv


class CustomDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = "s"
    delimiter = "?"
    lineterminator = '\n'


csv.register_dialect('How are you doing', CustomDialect)

with open('How are you doing.csv', 'w') as f:
    writer = csv.writer(f, dialect='How are you doing')
    for _ in range(6):
        writer.writerow(['1', '2', '3'])

with open('How are you doing.csv', 'r') as f:
    reader = csv.reader(f, dialect='How are you doing')
    for row in reader:
        print(row)
