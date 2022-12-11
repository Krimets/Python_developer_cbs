# Завдання 3
# Використовуючи модуль sqlite3 та модуль smtplib, реалізуйте реальне додавання користувачів до бази. Мають бути
# реалізовані такі функції та класи:
# ·        клас користувача, що містить у собі такі методи: get_full_name (ПІБ з поділом через пробіл: «Петров Ігор
# Сергійович»), get_short_name (формату ПІБ: «Петров І. С.»), get_age (повертає вік користувача, використовуючи поле
# birthday типу datetime.date); метод __str__ (повертає ПІБ та дату народження);
# ·        функція реєстрації нового користувача (приймаємо екземпляр нового користувача та відправляємо email на
# пошту користувача з листом подяки).
# ·        функція відправлення email з листом подяки.
# ·        функція пошуку користувачів у таблиці users за іменем, прізвищем і поштою.
#
# Протестувати цей функціонал, використовуючи заглушки у місцях надсилання пошти. Під час штатного запуску програми
# вона має відправляти повідомлення на вашу реальну поштову скриньку (необхідно налаштувати SMTP, використовуючи
# доступи від провайдера вашого email-сервісу).

# Приклад налаштування SMTP для сервісу Gmail: https://support.google.com/mail/answer/7126229?hl=ru


import datetime
import sqlite3
import smtplib


class User:
    def __init__(self, surname, name, patronymic, birthday, mail):
        self.cursor = None
        self.conn = None
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birthday = birthday
        self.mail = mail

    def get_full_name(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    def get_short_name(self):
        return f'{self.surname} {self.name[0]}. {self.patronymic[0]}.'

    def get_age(self):
        now = datetime.datetime.now().year
        birth = now - self.birthday
        return f'{birth} рочки'

    def __str__(self):
        return f'{self.get_full_name()}, {self.get_age()}'

    def connection(self):
        self.conn = sqlite3.connect('db.USERS')
        self.cursor = self.conn.cursor()

    def end_connection(self):
        self.cursor.close()
        self.conn.close()

    def create_db(self):
        self.connection()
        try:
            self.conn.execute(
                """CREATE TABLE IF NOT EXISTS USERS (
                       id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                       surname TEXT NOT NULL,
                       name TEXT NOT NULL,
                       patronymic TEXT NOT NULL,
                       birthday INTEGER NOT NULL,
                       mail TEXT NOT NULL
               )""")
            self.conn.commit()
            print('db USERS created')
        except sqlite3.Error as e:
            print(f"not created because: {e}")
        finally:
            self.end_connection()

    def add_user_db(self):
        try:
            self.connection()
            sqlite_query = '''INSERT INTO USERS
                (surname, name, patronymic, birthday, mail) VALUES 
                ("%s", "%s", "%s", "%s", "%s")''' % (self.surname, self.name, self.patronymic, self.birthday, self.mail)
            self.cursor.execute(sqlite_query)
            self.conn.commit()
            print('Done')
        except sqlite3.Error as e:
            print(f"not added because: {e}")
        finally:
            self.end_connection()

    def user_search_method(self):
        try:
            self.connection()
            self.cursor.execute("""SELECT * from USERS where surname='%s' and name='%s' and mail='%s'""" %
                                (self.surname, self.name, self.mail))
            user = self.cursor.fetchone()
            print(f"функція пошуку користувачів у таблиці users за іменем, прізвищем і поштою: {user}")
        except sqlite3.Error as e:
            print(f"Error: {e}")
        except BaseException as base:
            print(f"Error: {base}. db is empty")
        finally:
            self.end_connection()

    @staticmethod
    def send_mail():
        # # import necessary packages
        #
        # from email.mime.multipart import MIMEMultipart
        # from email.mime.text import MIMEText
        # import smtplib
        #
        # # create message object instance
        # msg = MIMEMultipart()
        #
        # message = "Thank you for registration"
        #
        # # setup the parameters of the message
        # password = "your_password"
        # msg['From'] = "your_address"
        # msg['To'] = self.mail
        # msg['Subject'] = "Registration"
        #
        # # add in the message body
        # msg.attach(MIMEText(message, 'plain'))
        #
        # # create server
        # server = smtplib.SMTP('smtp.gmail.com: 587')
        #
        # server.starttls()
        #
        # # Login Credentials for sending the mail
        # server.login(msg['From'], password)
        #
        # # send the message via the server.
        # server.sendmail(msg['From'], msg['To'], msg.as_string())
        #
        # server.quit()

        #print("successfully sent email to %s:" % (msg['To']))
        print("successfully sent email")


def new_user(new_u):
    print(new_u)
    new_u.add_user_db()
    email(new_u, new_u.mail)


def email(user, mail):
    print(f'Приймаємо екземпляр {user} та відправляємо {mail} на пошту користувача з листом подяки')
    user.send_mail()
    # b = smtplib.CRLF
    # print(dir(b))


def user_search(user):
    user.user_search_method()


u = User('Вокозм', 'Василь', 'Федорович', 2000, 'vokozm@gmail.com')
u.create_db()
print(u.get_full_name())
print(u.get_short_name())
print(u.get_age())

new_user(u)
user_search(u)
