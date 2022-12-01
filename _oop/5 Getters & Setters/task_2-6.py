# Завдання 2
# Створити клас Contact з полями surname, name, age, mob_phone, email. Додати методи get_contact, sent_message.
# Створити клас-нащадок UpdateContact з полями surname, name, age, mob_phone, email, job. Додати методи get_message.
# Створити екземпляри класів та дослідити стан об'єктів за допомогою атрибутів: __dict__, __base__, __bases__.
# Роздрукувати інформацію на екрані.

# Завдання 3
# Використовуючи код з завдання 2, використати функції hassttr(), getattr(), setattr(), delattr().

# Завдання 4
# Використовуючи код з завдання 2, створити 2 екземпляри обох класів. Використати функції isinstance() – для перевірки
# екземплярів класу (за яким класом створені) та issubclass() – для перевірки і визначення класу-нащадка.

# Завдання 5
# Використовуючи код завдання 2 надрукуйте у терміналі інформацію, яка міститься у класах Contact та UpdateContact.
# Видаліть атрибут job, і знову надрукуйте стан класів.

# Завдання 6
# Використовуючи код завдання 2 надрукуйте у терміналі всі методи, які містяться у класі Contact.


class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        pass

    def sent_message(self):
        pass


class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        pass


print('\ntask 2')
c = Contact('Шевченко', 'Андрій', 30, '+380666666666', 'Shevchenko@gmail.com')
up_c = UpdateContact('Чумак', 'Юрій', 60, '+380777777777', 'Chumak@gmail.com', 'Пекар')
print(c.__dict__)
print(up_c.__dict__)
print(Contact.__base__)
print(Contact.__bases__)
print(UpdateContact.__base__)
print(UpdateContact.__bases__)

print('\ntask 3 + task 5')
print(hasattr(c, 'job'))
print(hasattr(up_c, 'job'))
setattr(c, 'name', 'Ivan')
setattr(up_c, 'name', 'Ivan2')
print(getattr(c, 'name'))
print(getattr(up_c, 'name'))

print(up_c.__dict__)
delattr(up_c, 'job')
print(up_c.__dict__)

print('\ntask 4')
print(isinstance(c, Contact))
print(isinstance(c, UpdateContact))
print(isinstance(up_c, Contact))
print(isinstance(up_c, UpdateContact))
print(issubclass(Contact, UpdateContact))

print('\ntask 6')
print(Contact.__dict__)
