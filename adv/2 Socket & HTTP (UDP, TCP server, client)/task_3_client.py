# Завдання 3
# Створіть сокет, який приймає повідомлення з двома числами, що розділені комою. Сервер має конвертувати рядкове
# повідомлення у два числа й обчислювати його суму. Після успішного обчислення повертати відповідь клієнту.

from socket import socket, AF_INET, SOCK_STREAM

massage = input()
m = massage.split(',')
with socket(AF_INET, SOCK_STREAM) as sock:
    sock.connect(('127.0.0.1', 9999))
    sock.send(massage.encode('utf-8'))
    answer = sock.recv(1024).decode('utf-8')
    print(f'Done: {m[0]} + {m[1]} = {answer}')
