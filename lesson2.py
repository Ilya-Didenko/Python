#1. Получить количество учеников с сайта geekbrains.ru:

#a) при помощи регулярных выражений,

import requests
import re
from bs4 import BeautifulSoup as BS

code = requests.get('https://geekbrains.ru/')
text = code.text
print (text)

li = re.findall('<span class="total-users">Нас уже (.+) человек</span>', text)
print ('Кол-во cтудентов:',li[0])

#b) при помощи библиотеки BeautifulSoup.

soup = BS(text, 'html.parser')
students = soup.find(class_='total-users').text
students_clear = re.sub('[^\d,\s ]', '', students)
print ('Кол-во cтудентов:',students_clear)

