# Завдання 1
# Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані?
# Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).

class Car:
    def __init__(self):
        self.__brand = 'TESLA'
        self.__model = 'MODEL S'
        self.__year = '2022'
        self.color = 'black'
        self.price = 220000

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year


my_car = Car()

print(my_car.get_brand())
print(my_car.get_model())
print(my_car.get_year())
print(my_car.color)
print(my_car.price)

my_car.set_brand('HONDA')
my_car.set_model('CIVIC')
my_car.set_year('1998')
my_car.color = 'red'
my_car.price = 3000
print()

print(my_car.get_brand())
print(my_car.get_model())
print(my_car.get_year())
print(my_car.color)
print(my_car.price)
