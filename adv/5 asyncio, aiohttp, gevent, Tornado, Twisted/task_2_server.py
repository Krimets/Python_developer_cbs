# Завдання 2
# Розробіть сокет-сервер на основі бібліотеки asyncio.

import asyncio
from socket import socket, AF_INET, SOCK_STREAM

connects = [8888, 9999, 7777]


async def cron():
    tasks = [
        asyncio.ensure_future(cli(y))
        for y in connects
    ]
    for future in asyncio.as_completed(tasks):
        n = await future
        print(n)


async def cli(y):
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.bind(('127.0.0.1', y))
        sock.listen(3)
        client, addr = sock.accept()
        print(y, 'connected, reading message...')
        n = client.recv(1024).decode('utf-8')
        return n

event_loop = asyncio.run(cron())
