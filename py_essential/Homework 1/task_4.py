# Завдання 4
# Створіть клас, який описує автомобіль. Створіть клас автосалону, що містить в собі список автомобілів,
# доступних для продажу, і функцію продажу заданого автомобіля.

class Car:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    def __str__(self):
        return f'{self.brand}: {self.color}, {self.price}'

    def __repr__(self):
        return f'{self.brand}: {self.color}, {self.price}'


class CarShowroom:
    def __init__(self):
        self.cars = []

    def car_list(self, car):
        self.cars.append(car)

    def __str__(self):
        return f"Car list: {self.cars} \n"

    def __repr__(self):
        return f"Car list: {self.cars} \n"

    def sell_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f'Car {car} sold')
        else:
            print('Car not in sale')


car1 = Car("BMW", "Black", "$10000")
car2 = Car("Honda", "Red", "$12000")
car3 = Car("Mitsubishi", "White", "$9000")
my_car_list = [car1, car2, car3]
for i in my_car_list:
    print(i)

dealer = CarShowroom()
dealer.car_list(car1)
dealer.car_list(car2)
dealer.car_list(car3)
print(dealer, sep='\n')

dealer.sell_car(car1)
dealer.sell_car(car3)
print('\nleft', dealer, sep='\n')
