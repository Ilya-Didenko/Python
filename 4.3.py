# Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name — строка, полученная от пользователя,
# health = 100,
# damage = 50.
#
# Поэкспериментируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои.
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.

# подключаем модуль random
import random
# запрашиваем имена соперников выводим на экран
player = {'player': input('Введите ваше имя:'),
          'health': 200,
          'damage': 25}

enemy = {'player': input('Введите имя соперника:'),
         'health': 150,
         'damage': 40}

print('Создан игрок: ', player)
print('Создан соперник: ', enemy)

#создаем функцию отвечающую за нанесение урона
def attack(person1, person2):
    person2.update({'health': int(person2['health'] - person1['damage'])})
    return person2['health']

#создаем функцию хода игры с случайной генерацией очередности хода
def game():
    while True:
        who_step = bool(random.getrandbits(1))
        if who_step:
            attack(enemy, player)
            print('Остаток здоровья после удара у {} : {}'.format(player['player'], player['health']))
        else:
            attack(player, enemy)
            print('Остаток здоровья после удара у {} : {}'.format(enemy['player'], enemy['health']))
#проверяем условивия победы для выхода из цикла
        if player['health'] <= 0 or enemy['health'] <= 0:
            print('Игра окончена')
            if player['health'] > enemy['health']:
                print('Победил игрок',player)
            elif enemy['health'] > player['health']:
                print('Победил соперник', enemy)
            break

#вызываем функцию хода игры
game()