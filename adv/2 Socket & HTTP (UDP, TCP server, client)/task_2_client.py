# Завдання 2
# Створіть UDP-сервер, який очікує на повідомлення про нові пристрої в мережі. Він приймає повідомлення певного
# формату, де буде ідентифікатор пристрою, і друкує нові під'єднання в консоль. Створіть UDP-клієнта, який надсилатиме
# унікальний ідентифікатор пристрою на сервер, повідомляючи про свою присутність.

from socket import socket, AF_INET, SOCK_DGRAM

clients = ['phone', 'computer', 'laptop']

for _ in clients:
    massage = f'"{_}" connected'
    with socket(AF_INET, SOCK_DGRAM) as sock:
        sock.sendto(massage.encode('utf-8'), ('127.0.0.1', 8888))
