# Завдання 3
# Створіть сокет, який приймає повідомлення з двома числами, що розділені комою. Сервер має конвертувати рядкове
# повідомлення у два числа й обчислювати його суму. Після успішного обчислення повертати відповідь клієнту.

from socket import socket, AF_INET, SOCK_STREAM

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.bind(('127.0.0.1', 9999))
    sock.listen(2)

    while True:
        try:
            client, addr = sock.accept()
            n = client.recv(1024).decode('utf-8')
            x, y = n.split(',')
            s = int(x) + int(y)
        except ValueError as r:
            print('Error')
        else:
            print(s)
            client.send(str(s).encode('utf-8'))
        finally:
            print(f'Done')
