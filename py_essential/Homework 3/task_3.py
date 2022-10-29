# Завдання 3
# Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким засобом інкапсуляції, як властивості.
# Ознайомтеся з декоратором property у Python. Створіть клас, що описує температуру і дозволяє задавати та
# отримувати температуру за шкалою Цельсія та Фаренгейта, причому дані можуть бути задані в одній шкалі,
# а отримані в іншій.

class Temperature:
    def __init__(self):
        self.__scale = 'c'
        self.__value = 0

    @staticmethod
    def ftoc(v):
        return (v * 9 / 5) + 32

    @staticmethod
    def ctof(v):
        return (v - 32) * 5 / 9

    @property
    def temp(self):
        return f'Temperature = {self.__value, self.__scale}'

    def set_temp(self, value, scale, change=None):
        if scale == 'f' and change == 'change':
            self.__value = self.ctof(int(value))
            self.__scale = 'c'
        elif scale == 'c' and change == 'change':
            self.__value = self.ftoc(int(value))
            self.__scale = 'f'
        else:
            self.__value = value
            self.__scale = scale


t1 = Temperature()
t1.set_temp(23, 'c', 'change')
print(t1.temp)
t1.set_temp(103, 'f')
print(t1.temp)
t1.set_temp(103, 'f', 'change')
print(t1.temp)
t1.set_temp(3, 'c')
print(t1.temp)
