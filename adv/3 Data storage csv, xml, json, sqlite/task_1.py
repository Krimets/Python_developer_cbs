# Завдання 1
# Створіть прості словники та конвертуйте їх у JSON. Збережіть JSON у файлі та спробуйте завантажити дані з файлу.

import json

data = {"first name": "Alexander", "last name": "Krimets"}

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    data_new = json.load(f)

print(data_new)
