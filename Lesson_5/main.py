# Создайте модуль main.py. Из модулей, реализованных в заданиях 1 и 2, сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте, что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.

# импорт модуля randoms и использование функции из него
import randoms
numbers = [1,2,3,4]
randoms.win_number(numbers)

#вызов отдельных функций из модуля dir и их использование
from dir import create_dir, delet_dir
create_dir()
delet_dir()