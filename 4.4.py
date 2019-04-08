#Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр — armor = 1.2 (величина брони персонажа)
#Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
#Следовательно, у вас должно быть 2 функции:
#1. Наносит урон. Это улучшенная версия функции из задачи 3.
#2. Вычисляет урон по отношению к броне.

# подключаем модуль random
import random
# запрашиваем имена соперников выводим на экран
player = {'player': input('Введите ваше имя:'),
          'health': 150,
          'damage': 35,
          'armor': 1.2}

enemy = {'player': input('Введите имя соперника:'),
         'health': 150,
         'damage': 35,
         'armor': 1.2}

print('Создан игрок: ', player)
print('Создан соперник: ', enemy)

#создаем функцию отвечающую за нанесение урона, c учетом брони
def attack(person1, person2):
    person2.update({'health': int(person2['health'] - person1['damage']/person1['armor'])})
    return person2['health']

# создаем функцию зотвечающую за случайное повреждение брони
def damage_armor(person1):
    person1.update({'armor': round(person1['armor'] - random.uniform(0.0,0.1),1)})
    if person1['armor'] < 1:
        person1.update({'armor':1})
    return person1['armor']

#создаем функцию хода игры с случайной генерацией очередности хода и вызовом функции прреждения брониб если она еще цела
def game():
    while True:
        who_step = bool(random.getrandbits(1))
        if who_step:
            if player['armor'] > 1:
                damage_armor(player)
            else:
                attack(enemy, player)
            print('Остаток здоровья и брони после удара у {} : {} : {}'.format(player['player'], player['health'], player ['armor']))
        else:
            if enemy['armor'] > 1:
                damage_armor(enemy)
            else:
                attack(player, enemy)
            print('Остаток здоровья и брони после удара у {} : {} : {}'.format(enemy['player'], enemy['health'], player ['armor']))
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