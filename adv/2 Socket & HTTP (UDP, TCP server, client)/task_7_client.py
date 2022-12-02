# Завдання 7
# Створити простий чат на основі протоколу TCP, який дасть змогу під'єднуватися кільком клієнтам та обмінюватися
# повідомленнями.

import socket
import threading

name = input('Write your name: \n')

HOST = '127.0.0.1'
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "What's your name?":
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = input()
        if message == 'exit':
            client.close()
            break
        else:
            client.send(f'{name}: {message}'.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()