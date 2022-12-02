"""
При зчитуванні об'єкта datetime з таблиці SQLite необхідно отримати об'єднуючий тип - datetime.
"""

import sqlite3
import datetime


def add_developer(dev_id, name, joining_date):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db',
                                            detect_types=sqlite3.PARSE_DECLTYPES |
                                            sqlite3.PARSE_COLNAMES)
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")

        sqlite_create_table_query = '''CREATE TABLE new_developers2 (
                                       id INTEGER PRIMARY KEY,
                                       name TEXT NOT NULL,
                                       joiningDate timestamp);'''

        cursor.execute(sqlite_create_table_query)

        # вставити дані розробника
        sqlite_insert_with_param = """INSERT INTO 'new_developers2'
                          ('id', 'name', 'joiningDate')
                          VALUES (?, ?, ?);"""

        data_tuple = (dev_id, name, joining_date)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Розробник успішно доданий\n")

        # отримати дані розробника
        sqlite_select_query = """SELECT name, joiningDate from new_developers2 where id = ?"""
        cursor.execute(sqlite_select_query, (1,))
        records = cursor.fetchall()

        for row in records:
            developer = row[0]
            joining_date = row[1]
            print(developer, "приєднався", joining_date)
            print("тип дати", type(joining_date))
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


add_developer(1, 'Mark', datetime.datetime.now())
# В результаті дані з таблиці, що повернулися, представлені типом datetime.datetime.
