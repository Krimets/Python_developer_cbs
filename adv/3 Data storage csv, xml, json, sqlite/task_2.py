# Завдання 2
# Створіть XML-файл із вкладеними елементами та скористайтеся мовою пошуку XPATH. Спробуйте здійснити пошук
# вмісту за створеним документом XML, ускладнюючи свої запити та додаючи нові елементи, якщо буде потрібно.
from xml.etree import ElementTree as ET

data = [
    {'name': 'Steve', 'age': 29, 'mark': 90},
    {'name': 'Kerl', 'age': 28, 'mark': 91},
    {'name': 'Alex', 'age': 27, 'mark': 92},
    {'name': 'Mike', 'age': 26, 'mark': 93},
    {'name': 'John', 'age': 25, 'mark': 94},
]
root = ET.Element('data')
for item in data:
    record = ET.SubElement(root, 'person')
    for key, value in item.items():
        e = ET.SubElement(record, key)
        e.text = str(value)
tree = ET.ElementTree(root)
tree.write('data.xml', encoding='utf-8')


tree = ET.parse('data.xml')
root = tree.getroot()

names = root.findall('./person/name')
ages = root.findall('./person/age')
marks = root.findall('./person/mark')

# збираємо теги у спільні групи та створюємо спільний словник для кожного person.
for values in zip(names, ages, marks):
    row = {value.tag: value.text for value in values}
    print(row)
