# Завдання 3
# Створіть ієрархію класів із використанням множинного успадкування. Виведіть на екран порядок вирішення методів
# для кожного класу. Поясніть, чому лінеаризація даних класів виглядає саме так.

class A:
    def __init__(self):
        self.a = 10

    def method_a(self):
        print(self.a * 2)


class D(A):
    def __init__(self):
        A.__init__(self)
        self.d = 10

    def method_d(self):
        print(self.a * self.d)


class B(A):
    def __init__(self):
        A.__init__(self)
        self.b = 5

    def method_b(self):
        print(self.b + self.a)


class C(B, D):
    def __init__(self, c):
        B.__init__(self)
        D.__init__(self)
        self.c = c

    def method_c(self):
        print(self.a * self.d * self.b + self.c)


coo1 = A()
coo1.method_a()
coo2 = B()
coo2.method_b()
coo3 = D()
coo3.method_d()
coo4 = C(59)
coo4.method_c()
