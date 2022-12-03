# Завдання 2
# Створіть три функції, одна з яких читає файл на диску із заданим ім'ям та перевіряє наявність рядка «Wow!».
# Якщо файлу немає, то засипає на 5 секунд, а потім знову продовжує пошук по файлу. Якщо файл є, то відкриває його і
# шукає рядок «Wow!». За наявності цього рядка закриває файл і генерує подію, а інша функція чекає на цю подію і у
# разі її виникнення виконує видалення цього файлу. Якщо рядки «Wow!» не було знайдено у файлі, то засипати на
# 5 секунд. Створіть файл руками та перевірте виконання програми.

import threading
import time
import os

b = 'Wow!'
timer = 100


def stoper():
    time.sleep(3)
    print('Stoper starting')
    global timer
    while timer > 0:
        time.sleep(1)
        timer -= 1
        print(timer)
    print('Stoper stoping')


def writer():
    time.sleep(10)
    while timer > 0:
        try:
            with open('wow.txt', 'w') as f:
                f.write(b)
            print('Writer writing "Wow!"')
        except:
            print('Writer sleeping')
        time.sleep(20)


def reader():
    while timer > 10:
        time.sleep(5)
        try:
            with open('wow.txt', 'r') as f:
                txt = f.read()
            if txt == b:
                print('Reader find "Wow!"')
                product.set()
                product.clear()
        except:
            time.sleep(5)
            print('Reader sleeping')


def deleter():
    while timer > 20:
        print('Deleter waiting')
        product.wait()
        file_name = 'wow.txt'
        cur_dir = os.getcwd()
        file_list = os.listdir(cur_dir)
        if file_name in file_list:
            print('Deleter delete "Wow!"')
            os.remove(file_name)
        else:
            time.sleep(5)
            print('Deleter sleeping')


product = threading.Event()

task1 = threading.Thread(target=reader)
task2 = threading.Thread(target=deleter)
task3 = threading.Thread(target=writer)
task4 = threading.Thread(target=stoper)

task1.start()
task2.start()
task3.start()
task4.start()

task1.join()
task2.join()
task3.join()
task4.join()
