# Завдання 3
# Створіть список товарів в інтернет-магазині. Серіалізуйте його за допомогою pickle та збережіть у JSON.

import json
import pickle

data = ['Samsung Galaxy M32', 'Apple iPhone 14', 'Motorola G32']
data_new = {}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)

for index, value in enumerate(data):
    data_new[index] = value

with open('data.json', 'w') as f:
    json.dump(data_new, f)
