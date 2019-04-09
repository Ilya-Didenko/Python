#Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

#создаемфункцию, описываем условия отбора максимального числа из трех
def print_max(number1, number2, number3):
    if number1  > number2:
        result = number1
    else:
        result = number2
    if number3 > result:
        result = number3
    print(f'Максимальное число из введнных : {result}')
#запрашиваем данные
number1 = input('Введите первое число: ')
number2 = input('Введите первое число: ')
number3 = input('Введите первое число: ')
#вызываем функцию
print_max (number1, number2, number3)