class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_age_and_name(self):
        return self.age, self.name

    def say_hello(self):
        print(f'Hello, my name is {self.name}, i am {self.age} and {self.gender}')


class Human2(Human):
    def __init__(self, name, age, gender, h_color):
        super().__init__(name, age, gender)
        self.h_color = h_color


person1 = Human(name='John', age=25, gender='male')
person2 = Human2(name='Anna', age=35, gender='female', h_color='yellow')
print(person1.age)
print(person1.get_gender())
print(person1.get_age_and_name())

person1.say_hello()
person2.say_hello()

print(person2.h_color)


class A:
    def __init__(self):
        self.a = 10


class B:
    def __init__(self):
        self.b = 5


class C(A, B):
    def __init__(self):
        # super().__init__()
        A.__init__(self)
        B.__init__(self)


coo = C()
print(coo.a)
print(coo.b)
