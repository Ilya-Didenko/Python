#Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
#Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»


#создаем функцию которая будет возаращать строку с данными:
def print_data(name, age, city):
    print(f'{name}, {age} год(а), проживает в городе  {city}')
#запрашиваем данные:
name = input('Вдеите имя: ')
age = int(input('Введите возвраст: '))
city = input('Вдеите город проживания: ')
#вызываем функцию
print_data(name, age, city)