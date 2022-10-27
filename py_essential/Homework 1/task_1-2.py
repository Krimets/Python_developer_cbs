# Завдання 1
# Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та жанр.
# Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.

# Завдання 2
# Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків.
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.

class BookComment:
    def __init__(self, user, comment):
        self.user = user
        self.comment = comment

    def __str__(self):
        return f'\n{self.user} writes about book:\n{self.comment}'

    def __repr__(self):
        return f'\n{self.user} writes about book:\n{self.comment}'


class Book:
    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
        self.comments = []

    def add_comment(self, user, comment):
        self.comments.append(BookComment(user, comment))

    def __str__(self):
        return f"A {self.genre} book {self.name}, written by {self.author} in {self.year},\n{self.comments}\n"

    def __repr__(self):
        return f"A {self.genre} book {self.name}, written by {self.author} in {self.year},\n{self.comments}\n"


book1 = Book('JK Rowling', "Harry Potter and the Philosopher's Stone", 1997, 'fantasy')
book1.add_comment('Petya', 'Very good book')
book1.add_comment('Vova', 'Nice')
book1.add_comment('Ira', 'Impressive')
# print(book1.__str__())
book2 = Book('JK Rowling', "Harry Potter And The Chamber of secrets", 1998, 'fantasy')
book2.add_comment('Petya', 'norm.')
book2.add_comment('Vova', 'Perfect')
book2.add_comment('Ira', 'Wow')
# print(book2.__str__())
book3 = Book('JK Rowling', "Harry Potter and the prisoner of Azkaban", 1999, 'fantasy')
book3.add_comment('Petya', 'So so')
book3.add_comment('Vova', 'Not bad')
book3.add_comment('Ira', 'Super')
# print(book3.__repr__())

my_list = [book1, book2, book3]
for i in my_list:
    print(i)
