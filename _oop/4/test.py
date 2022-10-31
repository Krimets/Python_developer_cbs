counter = 0
counter2 = 0
s = []


class UserException(Exception):
    def __init__(self, text):
        self.text = text


while len(s) < 5:
    try:
        a = int(input('Введіть значення '))
        if a < 0:
            counter += 1
            raise UserException('Значення негативне')
        s.append(a)
    except UserException as e:
        print(e)
    except:
        counter2 += 1
        print("Помилка вводу данних")
    finally:
        print('\nВаш список:', s)
        print('Негативних значень:', counter)
        print('Помилок вводу:', counter2)
