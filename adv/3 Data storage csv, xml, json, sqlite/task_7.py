# Завдання 7
# Створіть функцію, яка формує CSV-файл на основі даних, введених користувачем через консоль. Файл має містити
# такі стовпчики: імена, прізвища, дати народження та місто проживання. Реалізуйте можливості перезапису цього
# файлу, додавання нових рядків до наявного файлу, рядкового читання з файлу та конвертації всього вмісту у
# формати та JSON.

import csv
import json


class Task7:
    def __init__(self):
        self.names = ['name', 'surname', 'birthdate', 'city']
        self.data = []

    def create_csv(self):
        with open('task7.csv', 'w') as f:
            writer = csv.writer(f)
            for _ in range(4):
                dat = input(f'Input your data({self.names[_]})\n>>> ')
                self.data.append(dat)
            writer.writerow(self.names)
            writer.writerow(self.data)
            self.data = []

    def write_csv(self):
        with open('task7.csv', 'a') as f:
            writer = csv.writer(f)
            f.seek(2)
            for _ in range(4):
                dat = input(f'Input your data({self.names[_]})\n>>> ')
                self.data.append(dat)
            writer.writerow(self.data)
            self.data = []

    @staticmethod
    def read_csv():
        with open('task7.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

    @staticmethod
    def json_convert():
        with open('task7.csv', 'r') as f:
            reader = csv.DictReader(f)
            with open('task7.json', 'w') as fi:
                for row in reader:
                    json.dump(row, fi)
                    jdata = json.dumps(row, indent=4)
                    print('Convert done')
                    print(jdata)


master = Task7()
master.create_csv()
master.read_csv()
master.write_csv()
master.read_csv()
master.create_csv()
master.read_csv()
master.json_convert()
