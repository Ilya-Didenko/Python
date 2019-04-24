# 1.Получите текст из файла.


import re

with open ('text.txt', 'rb') as li:
    li1 = li.read()
    li2 = li1.decode('utf-8')
    print (li2)

# 2. Разбейте текст на предложения.

li3 = re.split ('\.\s', li2)

print (li3)

#3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.

li4 = re.findall('[а-яА-Я]{4,}', li2)

max_number = 0
max_word = None
for word in li4:
    number = li4.count(word)
    if max_number < number:
        max_number = number
        max_word = word

print ('Самая используемая форма слова, состоящая из 4 и более букв: "', max_word, '" Встречается в тексте - ', max_number, 'раза.')


#4. Отберите все ссылки.

li5 = re.findall ('\d\)\s(\w*\.?\w+\.ru\/?\w*)',li2)

print (li5)


#5. Ссылки на страницы какого домена встречаются чаще всего?

li6 = str(li5.copy())
li7 = re.findall ('(\w+)\.ru',li6)

max_number2 = 0
max_domen = None
for domen in li7:
    number2 = li7.count(domen)
    if max_number2 < number2:
        max_number2 = number2
        max_domen = domen

print ('Чаще всего (',max_number2,'раза )','встречаются ссылки на страницы: "',max_domen,'.ru "')


#6. Замените все ссылки на текст «Ссылка отобразится после регистрации».

new_text = re.sub('[^@\s](\w*\.?\w+\.ru\/?\w*)','«Ссылка отобразится после регистрации»',li2)

print (new_text)