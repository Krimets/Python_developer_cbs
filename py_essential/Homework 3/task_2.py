# Завдання 2
# Створіть 2 класи мови, наприклад, англійська та іспанська. В обох класів має бути метод greeting().
# Обидва створюють різні привітання. Створіть два відповідні об'єкти з двох класів вище та викличте дії
# цих двох об'єктів в одній функції (функція hello_friend).

class English:
    @staticmethod
    def greeting():
        print('Hello friend')


class Spanish:
    @staticmethod
    def greeting():
        print('Hola amigo')


def hello_friend():
    english_man.greeting()
    hombre_espanol.greeting()


english_man = English()
hombre_espanol = Spanish()

hello_friend()
