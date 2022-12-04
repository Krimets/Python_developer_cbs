# Завдання 1
# Створіть співпрограму, яка отримує контент із зазначених посилань і логує хід виконання в database, використовуючи
# стандартну бібліотеку requests, а потім проробіть те саме з бібліотекою aiohttp. Кроки, які мають бути
# залоговані: початок запиту до адреси X, відповідь для адреси X отримано зі статусом 200. Перевірте хід виконання
# програми на >3 ресурсах і перегляньте послідовність запису логів в обох варіантах і порівняйте результати.
# Для двох видів завдань використовуйте різні файли для логування, щоби порівняти отриманий результат.

import asyncio
import sqlite3
from datetime import datetime
import aiohttp
import requests

resources = [
    'https://jsonplaceholder.typicode.com/todos/1',
    'http://example.com',
    'https://github.com',
    'https://jsonplaceholder.typicode.com/posts/1',
]


async def fetch_url(url):
    async with aiohttp.request('get', url) as request:
        started = datetime.now()
        answer = request.status
        return url, await request.text(), started, answer


async def async_main():
    print('async started')
    conn = sqlite3.connect('db.async')
    cursor = conn.cursor()
    try:
        conn.execute(
            """CREATE TABLE IF NOT EXISTS async (
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   url NOT NULL,
                   started_time NOT NULL,
                   answer NOT NULL,
                   finished_time NOT NULL
           )""")
        print('async db connected')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error because: {e}")
    finally:
        cursor.close()
        conn.close()
    tasks = [
        asyncio.ensure_future(fetch_url(url))
        for url in resources
    ]
    for future in asyncio.as_completed(tasks):
        url, _, started, answer = await future
        finished = datetime.now()
        conn = sqlite3.connect('db.async')
        cursor = conn.cursor()
        try:
            sqlite_query = '''INSERT INTO async
                                (url, started_time, answer, finished_time) VALUES 
                                ("%s", "%s", "%s", "%s")''' % (url, started, answer, finished)
            cursor.execute(sqlite_query)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error because: {e}")
        finally:
            cursor.close()
            conn.close()
        print(url)
        print(started)
        print(answer)
        print(finished)
    print('async finished\n')


def sync_main():
    print('sync started')
    conn = sqlite3.connect('db.sync')
    cursor = conn.cursor()
    try:
        conn.execute(
            """CREATE TABLE IF NOT EXISTS sync (
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   url NOT NULL,
                   started_time NOT NULL,
                   answer NOT NULL,
                   finished_time NOT NULL
           )""")
        print('sync db connected')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error because: {e}")
    finally:
        cursor.close()
        conn.close()

    for url in resources:
        started = datetime.now()
        resp = requests.get(url)
        answer = resp.status_code
        finished = datetime.now()
        conn = sqlite3.connect('db.sync')
        cursor = conn.cursor()
        try:
            sqlite_query = '''INSERT INTO sync
                                            (url, started_time, answer, finished_time) VALUES 
                                            ("%s", "%s", "%s", "%s")''' % (url, started, answer, finished)
            cursor.execute(sqlite_query)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error because: {e}")
        finally:
            cursor.close()
            conn.close()
        print(url)
        print(started)
        print(answer)
        print(finished)
    print('sync finished\n')


sync_main()
event_loop = asyncio.run(async_main())
