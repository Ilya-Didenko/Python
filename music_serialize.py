# Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}

#С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.

# Подключаем модули для сериализации
import pickle, json

# Создаем словарь
my_favourite_group = {
'name': 'ЕСТЬ ЕСТЬ ЕСТЬ',
'tracks': ['Осень', 'Парсеки'],
'Albums': [{'name': 'Дорогой мой человек','year': 2011},
{'name': 'Сказки для Кейто','year': 2016}]}

# Создаем и открывае файл, в который сохраним результат в байтах
with open('group.pickle', 'wb') as f:
# Сохраняем объект в байтах
    pickle.dump(my_favourite_group, f)
# Выводим результат в байтах
with open ('group.pickle', 'rb') as f:
    result = f.read()
#print (result)

# Создаем и открывае файл, в который сохраним результат в формате json
with open('group.json', 'w', encoding= 'utf-8') as f:
# Сохраняем объект в формате json
    json.dump(my_favourite_group, f)
# Выводим результат в формате json
with open ('group.json', 'rb') as f:
    result = f.read()
#print (result)


