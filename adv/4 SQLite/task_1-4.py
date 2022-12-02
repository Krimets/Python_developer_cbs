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


class Db:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.pro = 0
        self.exp = 0

    def connection(self):
        self.conn = sqlite3.connect('db.sqlite3')
        self.cursor = self.conn.cursor()

    def end_connection(self):
        self.cursor.close()
        self.conn.close()

    def show(self):
        try:
            self.connection()
            self.cursor.execute("""SELECT * from exp""")
            total_rows = self.cursor.fetchall()
            print("All data: ", total_rows)
        except sqlite3.Error as e:
            print(f"Error: {e}")
        except BaseException as base:
            print(f"Error: {base}. db is empty")
        finally:
            self.end_connection()

    def total_exp(self):
        try:
            self.connection()
            data = self.conn.execute('SELECT * FROM exp WHERE destination="expense"').fetchall()
            for i in data:
                self.exp += int(i[2])
        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            print('All expense:', self.exp)
            self.exp = 0
            self.end_connection()

    def total_pro(self):
        try:
            self.connection()
            data = self.conn.execute('SELECT * FROM exp WHERE destination="profit"').fetchall()
            for i in data:
                self.pro += int(i[2])
        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            print('All profit:', self.pro)
            self.pro = 0
            self.end_connection()

    def create_db(self):
        self.connection()
        try:
            self.conn.execute(
                """CREATE TABLE exp (
                       id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                       destination TEXT NOT NULL,
                       amount INTEGER NOT NULL,
                       time NOT NULL
               )""")
            print('db created')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"not created because: {e}")
        finally:
            self.end_connection()

    def add_to_db(self, destination, amount, time):
        try:
            self.connection()
            sqlite_query = '''INSERT INTO exp
                    (destination, amount, time) VALUES ("%s", "%s", "%s")''' % (destination, amount, time)
            self.cursor.execute(sqlite_query)
            self.conn.commit()
            print('done')
        except sqlite3.Error as e:
            print(f"not added because: {e}")
        finally:
            self.end_connection()


if __name__ == '__main__':
    my_db = Db()
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
                my_db.create_db()
            case '2':
                my_db.add_to_db(input('profit|expense?\n>>> '),
                                input('How much?\n>>> '), input('day\n>>> '))
            case '3':
                my_db.total_exp()
            case '4':
                my_db.total_pro()
            case '5':
                my_db.show()
            case '6':
                print("bye")
                break
            case _:
                print("Choose from the menu")
                continue
