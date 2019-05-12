#1. Написать функцию получения IATA-кода города из его названия, используя API Aviasales.

import requests
import json


def iata_city (city):

    link = 'https://www.travelpayouts.com/widgets_suggest_params?q=Из%20'+city+'%20в%20Лондон'
    data = json.loads(requests.get(link).text)
    return data ['origin']['iata']



r = iata_city(city = input('Введите город:\n'))
print ('IATA код:',r)