
from socket import socket, AF_INET, SOCK_STREAM
from time import sleep

clients = {'phone': 8888, 'computer': 9999, 'laptop': 7777}

for _ in clients:
    sleep(2)
    massage = f'"{_}" connected, port = {clients[_]}'
    print(f'"{_}" will connected, port = {clients[_]}')
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(('127.0.0.1', clients[_]))
        sock.send(massage.encode('utf-8'))
print('All gadgets connected')
