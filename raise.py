# Написать функцию, которая принимает на вход число от 1 до 100.
# Если число равно 13, функция поднимает исключительную ситуации ValueError, иначе возвращает введенное число,
# возведенное в квадрат.
# Далее написать основной код программы. Пользователь вводит число.
# Введенное число передаем параметром в написанную функцию и печатаем результат, который она вернула.
# Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.



def you_number (number):
    global sqrt

    if number == 13:
        raise ValueError ('ERROR!')

    sqrt = number**2
    return sqrt


number = int(input ('Пожалуйста введитечисло от 0 до 100'))
you_number(number)
print(number,'^2=',sqrt)