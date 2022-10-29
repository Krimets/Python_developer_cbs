# Завдання 2
# Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може обробляти натискання миші.
# Опишіть клас кнопки. Створіть об'єкт кнопки та звичайного прямокутника. Викличте метод натискання на кнопку.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        print(f'Створено прямокутник зі сторонами {self.length} та {self.width}')


class Button:
    def __init__(self, device):
        self.device = device

    def push(self):
        print(f'Ви натиснули на кнопку на девайсі "{self.device}"')


square = Rectangle(length=100, width=50)
mouse = Button('компьютерна миша')
square.__str__()
mouse.push()
