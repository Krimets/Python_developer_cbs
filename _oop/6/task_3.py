# Завдання 3
# Напишіть ітератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).

class RevIt:
    def __init__(self, iterable, index=-1):
        self.iterable = iterable
        self.index = index

    def __next__(self):
        while True:
            try:
                print(self.iterable[self.index], end='')
                self.index -= 1
            except:
                print(' <<< end')
                break


i = RevIt(range(1, 101))
i.__next__()
