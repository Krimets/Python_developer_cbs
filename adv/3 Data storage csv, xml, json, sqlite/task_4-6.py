# Завдання 4
# Створіть таблицю «матеріали» з таких полів: ідентифікатор, вага, висота та додаткові характеристики матеріалу.
# Поле «додаткові  характеристики матеріалу» має зберігати у собі масив, кожен елемент якого є кортежем із двох
# значень: перше – назва характеристики, а друге – її значення.

# Завдання 5
# Для таблиці «матеріалу» з завдання 4 створіть користувальницьку агрегатну функцію, яка рахує середнє значення ваги
# всіх матеріалів вислідної вибірки й округляє значення до цілого.

# Завдання 6
# Для таблиці «матеріалу» з завдання 4 створіть функцію користувача, яка приймає необмежену кількість полів і повертає
# їх конкатенацію.

import csv
import random


class Task4:
    def __init__(self):
        self.materials = ['ідентифікатор', 'вага', 'висота', 'додаткові характеристики матеріалу']
        self.COLOURS = ['orange', 'red', 'black', 'white']
        self.data = []
        self.counter = 0
        self.concat = ''

    def create_materials(self):
        with open('materials.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(self.materials)
            for _ in range(10):
                self.data.append(random.choice(range(10000)))
                self.data.append(random.choice(range(1000)))
                self.data.append(random.choice(range(200)))
                self.data.append([("colour", random.choice(self.COLOURS)), ("price", random.choice(range(1000)))])
                writer.writerow(self.data)
                self.data = []
            print('>>> Materials create')
        with open('materials.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

    def weight_counter(self):
        with open('materials.csv', 'r') as f:
            for row in f:
                r = row.split(',')
                if r[1] != 'вага':
                    self.counter += int(r[1])
            print('>>> Значення ваги всіх матеріалів:', self.counter)
            self.counter = 0

    def conc(self, d):
        d = d.split(', ')
        for j in d:
            self.concat += str(j)
        print('>>> Повертає їх конкатенацію:', self.concat)
        self.concat = ''


shop = Task4()
shop.create_materials()
shop.weight_counter()
shop.conc('ідентифікатор, вага, висота, додаткові, характеристики, матеріалу, кількість')
