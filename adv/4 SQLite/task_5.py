# Завдання 5
# Create an Exchange Rates To USD db using API Monobank (api.monobank.ua). Do requests via request lib, parse
# results, write it into db. (2 examples required, Because there are no 3 examples if you look closely)
# Example:
# Table - Exchange Rate To USD:
#
# id (INT PRIMARY KEY) - 1, 2, 3, ...
# currency_name (TEXT) - UAH
# currency_value (REAL) - 39.5
# current_date (DATETIME) - 10/22/2022 7:00 PM

import json
import sqlite3
import requests


class ExchangeRateUSD:
    def __init__(self):
        self.currency_value = None
        self.conn = None
        self.cursor = None
        self.currency_name = 'UAH'
        self.URL = "https://api.monobank.ua/bank/currency"

    def connection(self):
        self.conn = sqlite3.connect('db.ExchangeRateUSD')
        self.cursor = self.conn.cursor()

    def end_connection(self):
        self.cursor.close()
        self.conn.close()

    def show(self):
        try:
            self.connection()
            self.cursor.execute("""SELECT * from ExchangeRateUSD""")
            total_rows = self.cursor.fetchall()
            print("All data: ", total_rows)
        except sqlite3.Error as e:
            print(f"Error: {e}")
        except BaseException as base:
            print(f"Error: {base}. db is empty")
        finally:
            self.end_connection()

    def create_db(self):
        self.connection()
        try:
            self.conn.execute(
                """CREATE TABLE IF NOT EXISTS ExchangeRateUSD (
                       id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                       currency_name TEXT NOT NULL,
                       currency_value REAL NOT NULL,
                       current_date DATETIME NOT NULL
               )""")
            self.conn.commit()
            print('db created')
        except sqlite3.Error as e:
            print(f"not created because: {e}")
        finally:
            self.end_connection()

    def parse(self, curr):
        if curr == 'USD':
            curr = 840
        if curr == 'EUR':
            curr = 978
        try:
            response = requests.get(self.URL)
            current_date = response.headers["Date"]
            data = json.loads(response.text)
            for i in data:
                if i['currencyCodeA'] == curr and i['currencyCodeB'] == 980:
                    self.currency_value = i['rateBuy']
            self.add_to_db(current_date)
        except:
            print("Too many requests!")

    def add_to_db(self, current_date):
        if self.currency_value:
            print(self.currency_value)
            try:
                self.connection()
                sqlite_query = '''INSERT INTO ExchangeRateUSD
                        (currency_name, currency_value, current_date) VALUES 
                        ("%s", "%s", "%s")''' % (self.currency_name, self.currency_value, current_date)
                self.cursor.execute(sqlite_query)
                self.conn.commit()
                self.currency_value = None
                print('Done')
            except sqlite3.Error as e:
                print(f"not added because: {e}")
            finally:
                self.end_connection()
        else:
            print('Need to parse first')


if __name__ == '__main__':
    my_db = ExchangeRateUSD()
    while True:
        ask = input("""
        Select an action:
        1 - create db
        2 - USD - UAH
        3 - EUR - UAH
        4 - show db
        5 - exit
        >>> """)
        match ask:
            case '1':
                my_db.create_db()
            case '2':
                my_db.parse('USD')
            case '3':
                my_db.parse('EUR')
            case '4':
                my_db.show()
            case '5':
                print("bye")
                break
            case _:
                print("Choose from the menu")
                continue
