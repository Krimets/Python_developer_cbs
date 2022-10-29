#Завдання 2
#Напишіть програму, яка обчислює значення функції 𝑦 = cos(3x), де - 𝜋 <= x <= 𝜋.

import math

x = float(input('Введiть значення x: '))
if -math.pi <= x <= math.pi:
    print('y =', math.cos(3 * x))
else:
    print('Значення не вiдповiдає параметрам, де - 𝜋 <= x <= 𝜋.')
