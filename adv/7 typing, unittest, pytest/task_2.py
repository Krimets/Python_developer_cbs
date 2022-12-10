# Завдання 2
# Створіть два класи Directory (тека) і File (файл) з типами (анотацією).
# Клас Directory має мати такі поля:
# ·        назва (name типу str);
# ·        батьківська тека (root типу Directory);
# ·        список файлів (список типу files, який складається з екземплярів File);
# ·        список підтек (список типу sub_directories, який складається з екземплярів Directory).
#
# Клас Directory має мати такі поля:
# ·        додавання теки до списку підтек (add_sub_directory, який приймає екземпляр Directory та присвоює поле root
# для приймального екземпляра);
# ·        видалення теки зі списку підтек (remove_sub_directory, який приймає екземпляр Directory та обнуляє поле
# root. Метод також видаляє теку зі списку sub_directories);
# ·        додавання файлу в теку (add_file, який приймає екземпляр File і присвоює йому поле directory – див. клас
# File нижче);
# ·        видалення файлу з теки (remove_file, який приймає екземпляр File та обнуляє у нього поле directory.
# Метод видаляє файл зі списку files).
#
# Клас File має мати такі поля:
# ·        назва (name типу str);
# ·        тека (Directory типу Directory).

import os
import shutil


class File:
    def __init__(self, file_name: str):
        self.file_name: str = file_name
        self.Directory: Directory


class Directory:
    def __init__(self, name: str):
        self.name: str = name
        self.root: Directory
        self.files: File
        self.sub_directories = os.listdir()

    def add_sub_directory(self):
        os.mkdir(self.name)

    def remove_sub_directory(self):
        shutil.rmtree(self.name)

    @staticmethod
    def add_file():
        open(fil.file_name, "w")

    @staticmethod
    def remove_file():
        os.remove(fil.file_name)


direct = Directory('New_dir')
fil = File('New_file.txt')
direct.add_sub_directory()
direct.remove_sub_directory()
direct.add_file()
direct.remove_file()
