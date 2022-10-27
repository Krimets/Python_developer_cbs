# Завдання 4
# Ознайомтеся за допомогою документації з класами namedtuple та deque модуля collections. Створіть фабрику
# іменованих кортежів оцінок для учнів однієї групи з предметів: алгебра, геометрія, історія, інформатика,
# географія. Вивести дані на екран.

from collections import namedtuple
from collections import deque

Marks = namedtuple('Оцінки', 'Алгебра Геометрія Історія Інформатика Географія')

ivan = Marks(12, 10, 11, 12, 9)
daria = Marks(10, 11, 12, 11, 10)
maxim = Marks(7, 9, 9, 8, 10)

study = deque([ivan, daria, maxim])

print("У Івана такі", ivan)
print("У Дарії такі", daria)
print("У Максима такі", maxim)

print(study)
