# Завдання 1
# Зробіть таблицю для підрахунку особистих витрат із такими полями: id, призначення, сума, час.

# Завдання 2
# Створіть консольний інтерфейс (CLI) на Python для додавання нових записів до бази даних.

# Завдання 3
# Змініть таблицю так, щоби можна було додати не лише витрати, а й прибутки.

# Завдання 4
# Створіть агрегатні функції для підрахунку загальної кількості  витрат i прибуткiв за місяць. Забезпечте
# відповідний інтерфейс користувача.

import sqlite3


def connection_cursor():
    conn = sqlite3.connect('db.sqlite3')  # (':memory:') #
    cursor = conn.cursor()
    return cursor


def show():
    cursor = connection_cursor().execute('SELECT * FROM "exp"')
    data = cursor.fetchall()
    print(data)
    cursor.close()


def total_exp():
    data = cursor.execute('SELECT * FROM exp WHERE destination="expense"').fetchall()
    print(data)


def total_pro():
    data = conn.execute('SELECT * FROM exp WHERE destination="profit"').fetchall()
    print(data)


def create_db():
    try:
        conn.execute(
            """CREATE TABLE exp (
                    id INTEGER PRIMARY KEY,
                    destination NOT NULL,
                    amount NOT NULL,
                    timex NOT NULL
            )""")
        print('db created')
    except sqlite3.Error as e:
        print("The database cannot be created.")
        print(f"not created because: {e}")


def add_to_db(id, destination, amount, timex):
    sqlite_query = '''INSERT INTO exp
                    (id, destination, amount, timex) VALUES ("%s", "%s", "%s", "%s")''' % (
    id, destination, amount, timex)
    cursor.execute(sqlite_query)
    print('done')


if __name__ == '__main__':
    while True:
        ask = input("""
        Select an action:
        1 - create db
        2 - add profit|expense
        3 - total expenses per month
        4 - total profits per month
        5 - show db
        6 - exit
        >>> """)
        match ask:
            case '1':
                create_db()
            case '2':
                add_to_db(input('id?\n>>> '), input('profit|expense?\n>>> '), input('How much?\n>>> '), input('month?\n>>> '))
            case '3':
                total_exp()
            case '4':
                total_pro()
            case '5':
                show()
            case '6':
                print("bye")
                cursor.close()
                conn.close()
                break
            case _:
                print("You must choose from the menu above.")
                continue
