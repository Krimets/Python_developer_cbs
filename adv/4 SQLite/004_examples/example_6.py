# Отримання змін з моменту підключення до БД
"""
Для статистики може знадобитися знайти кількість рядків бази даних, які були вставлені, видалені або змінені з
моменту відкриття з'єднання. Для цього використовується функція connection.total_changes sqlite3.
Цей метод повертає загальну кількість рядків, які торкнулися.
"""


import sqlite3


try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("Підключений до SQLite")

    sqlite_insert_query = """INSERT INTO sqlitedb_developers
                          (id, name, email, joining_date, salary)
                          VALUES (4, 'Alex', 'sale@gmail.com', '2020-11-20', 8600);"""
    cursor.execute(sqlite_insert_query)

    sql_update_query = """Update sqlitedb_developers set salary = 10000 where id = 4"""
    cursor.execute(sql_update_query)

    sql_delete_query = """DELETE from sqlitedb_developers where id = 4"""
    cursor.execute(sql_delete_query)

    sqlite_connection.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Помилка при роботі з SQLite", error)

finally:
    if sqlite_connection:
        print("Усього рядків, змінених після підключення до бази даних: ", sqlite_connection.total_changes)
        sqlite_connection.close()
        print("З'єднання з SQLite закрито")
