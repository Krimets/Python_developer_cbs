# Завдання 2
# Написати функцію, яка за допомогою регулярних виразів з файлу витягує дані про дату народження, телефон та
# електронну адресу. Дані потрібно записати до іншого файлу.

import re

a = 'IvanovIvan01-12-2000test123@gmail.comВідгукпрокурсиучня+380777777777'
with open('txt.txt', 'r') as file:
    txt = file.read()
result = re.findall(r'[\d\-]+|\+\d+|\w+@\w+\.com', txt)
print(result)


with open('txt2.txt', 'w') as file:
    file.write(str(result))
