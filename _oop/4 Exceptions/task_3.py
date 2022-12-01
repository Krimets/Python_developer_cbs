# Завдання 3
# Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи.
# Конструктор має генерувати виняток, якщо вказано неправильні дані. Введіть список працівників із клавіатури.
# Виведіть усіх співробітників, які були прийняті після цього року.

from random import choice  # імпортуємо choice з модулю random

# Створюємо списки працівників
n = ['Іван', 'Микола', 'Сергій', 'Олександр', 'Ганна', 'Світлана', 'Андрій', 'Вікторія']
s = ['Шевченко', 'Чумак', 'Мельник', 'Бакало', 'Андрусенко', 'Калиненко', 'Сиротенко', 'Диптан']
d = ['Закупівля', 'Логістика', 'Бухгалтерія', 'IT', 'Маркетинг', 'Кол-центр', 'Охорона']
y = [2022, 2000, 2030, 2001, 2002, 2003, 2023, 2024, 2025, 2010, 2011, 2020, 'колись', 'невідомо']
b = 0


# описуємо клас працівника
class Worker:
    def __init__(self, name, surname, department, year_of_employment):
        self.name = name
        self.surname = surname
        self.department = department
        self.year_of_employment = year_of_employment

    # метод для перевірки року прийняття на роботу
    def new(self):
        try:
            if self.year_of_employment > 2022:
                print(f'Майбутній працівник: {self.name} {self.surname}, Відділ - {self.department}, '
                      f'{self.year_of_employment} рік')
        except:
            print(f'>>> Данні вводяться з помилкою для: {self.name} {self.surname}, {self.department} '
                  f'"{self.year_of_employment}" - не вказано рік прийняття на роботу')


# генеруємо 20 випадкових працівників
while b < 21:
    b += 1
    w = Worker(choice(n), choice(s), choice(d), choice(y))
    w.new()
