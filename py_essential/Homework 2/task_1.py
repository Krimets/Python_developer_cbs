# Завдання 1
# Створіть клас Editor, який містить методи view_document та edit_document. Нехай метод edit_document виводить
# на екран інформацію про те, що редагування документів недоступне для безкоштовної версії. Створіть підклас
# ProEditor, у якому цей метод буде перевизначено. Введіть ліцензійний ключ із клавіатури та, якщо він коректний,
# створіть екземпляр класу ProEditor, інакше Editor. Викликайте методи перегляду та редагування документів.

class Editor:
    @staticmethod
    def view_document():
        print('Ви переглядаєте документ.')

    def edit_document(self):
        print('Вибачте, редагування документів недоступне для безкоштовної версії')


class ProEditor(Editor):
    def edit_document(self):
        print('Вітаю, редагування доступне')


user_key = input('Введіть ліцензійний ключ\n>>> ')
if user_key == '0123456789':
    doc1 = ProEditor()
else:
    doc1 = Editor()

doc1.view_document()
doc1.edit_document()
