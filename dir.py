# Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py).
# В нем напишите функцию, создающую директории от dir_1 до dir_9 в папке, из которой запущен данный код.
# Затем создайте вторую функцию, удаляющую эти папки.
# Проверьте работу функций в этом же модуле.

# Выpываем модуль os
import os

# Создаем функцию создающую дериктории.
def create_dir ():
        for i in range (1,10):
                new_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
                os.mkdir(new_path)
        return print('Директории созданы')
#вызываем функцию
#create_dir ()

# Создаем функцию удаляющую дериктории.
def delet_dir ():
        for i in range (1,10):
               new_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
               os.rmdir(new_path)
        return print('Директории удалены')
#вызываем функцию
#delet_dir ()