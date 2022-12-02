# Завдання 7
# Створити простий чат на основі протоколу TCP, який дасть змогу під'єднуватися кільком клієнтам та обмінюватися
# повідомленнями.

import socket
import threading

HOST = ''
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(9)
print("Server is running")

clients = []
names = []


def broadcast(message):
    """Function to forward the messages to other clients"""
    for client in clients:
        client.send(message)


def receive_and_fwd(client):
    """Function to receive messages from client"""
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            indx = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[indx]
            broadcast(f'{name} has left the chat room!'.encode('utf-8'))
            names.remove(name)
            break


def connect_client():
    """Function to handle the connection"""
    while True:
        client, address = server.accept()
        print(f'Connection with {str(address)} is established.')
        client.send(f"What's your name?".encode('utf-8'))
        name = client.recv(1024).decode('utf-8')
        names.append(name)
        clients.append(client)
        print(f"The name of the client is {name}")
        broadcast(f"{name} was connected to the chat".encode('utf-8'))
        client.send(f'You are now connected!'.encode('utf-8'))
        client.send(f'Persons in chat: {names}'.encode('utf-8'))
        thread = threading.Thread(target=receive_and_fwd, args=(client,))  # the thread needs to run for each client
        thread.start()


connect_client()
