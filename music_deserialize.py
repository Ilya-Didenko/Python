#Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
# Получить объект — словарь из предыдущего задания.

# Подключаем модули для десериализации
import pickle, json
# Открываем, читаем(десериализация) и сразу выводим информацию
with open('group.pickle', 'rb') as f:
    print (pickle.load(f))
# Открываем, читаем(десериализация) и сразу выводим информацию
with open('group.json', 'r') as f:
    print (json.load(f))
