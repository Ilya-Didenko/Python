# Напишите функцию, которая принимает на вход список.
# Функция создает из этого списка новый список из квадратных корней чисел (если число положительное) и самих чисел
# (если число отрицательное) и возвращает результат (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный список не должен измениться.


import math

numbers = [-1,  9, 5, -1, 12, -9, 22, 2, 1]
result = []

def sqrt_list(numbers):
    for number in numbers:
        result.append(math.sqrt(number)) if number > 0 else result.append(number)
    return print (numbers, '------>', result)

sqrt_list(numbers)