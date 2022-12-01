# Завдання 5
# Використовуючи код example_10, створіть декоратор @staticmethod для визначення повноліття людини в Україні та Америці.

# Завдання 6
# Використовуючи код example_10, створіть декоратори @classmethod для формування переліку об'єктів, які підрахують
# кількість повнолітніх людей в Україні та Америці.

from datetime import date


class MyClass1:
    def __init__(self, surname, name, age, country):
        self.surname = surname
        self.name = name
        self.age = age
        self.country = country

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear, country):
        return cls(surname, name, date.today().year - birthYear, country)

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))

    @staticmethod
    def full_age(name, age, country):
        if age >= 18 and country == 'Ukraine':
            print(f'{name} з {country} - Повнолітній')
        elif age >= 21:
            print(f'{name} з {country} - Повнолітній')
        else:
            print(f'{name} з {country} - Неповнолітній')

    @classmethod
    def from_country(cls, age, country):
        ukraine_full_age = 0
        usa_full_age = 0
        if age >= 18 and country == 'Ukraine':
            ukraine_full_age += 1
        elif age >= 21 and country == 'USA':
            usa_full_age += 1
        return ukraine_full_age, usa_full_age


class MyClass2(MyClass1):
    color = 'White'


m_per1 = MyClass1('Ivanenko', 'Ivan', 19, 'USA')
m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan',  2000, 'USA')
m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010, 'USA')
m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001, 'Ukraine')
m_per5 = MyClass2.fromBirthYear('Makus', 'Maksym', 2021, 'Ukraine')
m_per6 = MyClass2.fromBirthYear('Sydor', 'Anton', 23, 'Ukraine')
lst = [m_per1, m_per2, m_per3, m_per4, m_per5, m_per6]
ukr = 0
usa = 0

for i in lst:
    MyClass1.full_age(i.name, i.age, i.country)
    counter = MyClass1.from_country(i.age, i.country)
    ukr += counter[0]
    usa += counter[1]
print(f'Кількість повнолітніх людей в Україні = {ukr}, а в Америці = {usa}\n')

# m_per1.print_info()
# m_per2.print_info()
# print(isinstance(m_per3, MyClass2))
# print(isinstance(m_per4, MyClass1))
# print(issubclass(MyClass1, MyClass2))
# print(issubclass(MyClass2, MyClass1))
