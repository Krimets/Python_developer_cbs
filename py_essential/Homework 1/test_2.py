class Car:
    def __init__(self, brand, color, volume):
        self.brand = brand
        self.color = color
        self.volume = volume

    @staticmethod
    def drive():
        print('Forward')
        print('Backward')


class Car2(Car):
    @staticmethod
    def turn():
        print('Left')
        print('Right')


class Airplane:
    def __init__(self, model):
        self.model = model

    @staticmethod
    def up_land():
        print('fly')


class Dolores(Car2, Airplane):
    def __init__(self, brand, color, volume, model):
        Car2.__init__(self, brand, color, volume)
        Airplane.__init__(self, model)


fc = Dolores('Tesla', 'black', 10, 'F')
fc.up_land()
fc.drive()
fc.turn()
