# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# 1. Элемент кратен 3,
# 2. Элемент положительный,
# 3. Элемент не кратен 4.
#    Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа.
#    10-20 чисел в списке вполне достаточно.


numbers = [3, 5, 7, 9, 11, 12, 15, -9, -8, -6, -3, -1]

result = [i for i in numbers if i % 3 == 0 and i > 0 and i % 4 != 0]

print(result)