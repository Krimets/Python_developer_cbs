# Завдання 7
# Створіть ієрархію класів транспортних засобів. У загальному класі опишіть загальні всім транспортних засобів поля,
# у спадкоємцях – специфічні їм. Створіть кілька екземплярів. Виведіть інформацію щодо кожного транспортного засобу.

class Transport:
    def __init__(self, name):
        self.name = name

    def movement(self):
        print(f'{self.name} перевозить людей')
        print(f'{self.name} перевозить товари\n')


class GroundTransport(Transport):
    def __init__(self, g_transport):
        super().__init__(g_transport)
        self.g_transport = g_transport

    def ride(self):
        print(f'{self.g_transport} їздить по дорогам')


class AirTransport(Transport):
    def __init__(self, a_transport):
        super().__init__(a_transport)
        self.a_transport = a_transport

    def fly(self):
        print(f'{self.a_transport} літає')


class WaterTransport(Transport):
    def __init__(self, w_transport):
        super().__init__(w_transport)
        self.w_transport = w_transport

    def float(self):
        print(f'{self.w_transport} плаває')


class FutureTransport(GroundTransport, AirTransport, WaterTransport):
    def __init__(self, f_transport):
        GroundTransport.__init__(self, f_transport)
        AirTransport.__init__(self, f_transport)
        WaterTransport.__init__(self, f_transport)
        self.f_transport = f_transport


v = Transport('Транспорт')
v.movement()
v = GroundTransport('Наземний транспорт')
v.ride()
v.movement()
v = AirTransport('Повітряний транспорт')
v.fly()
v.movement()
v = WaterTransport('Водний транспорт')
v.float()
v.movement()
v = FutureTransport('Транспорт майбутнього')
v.ride()
v.fly()
v.float()
v.movement()
