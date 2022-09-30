# Pomóż szwajcarskiemu bankowi HSBC tworząc aplikację, która odczytuje i analizuje dane z Narodowego Banku Polskiego (NBP) udostępnione przez API i podaje ile była warta wskazana waluta we wskazanym dniu.

# Dzięki Tobie HSBC będzie mógł poprawnie wystawiać w Polsce faktury w walucie obcej - przepisy wymagają, aby kwoty na takich fakturach przeliczać na złotówki wg kursów NBP z określonych dni.

# 1. Zapoznaj się z opisem API: http://api.nbp.pl.
#    1. Ustal jak wygląda URL, pod którym znajdziesz kurs danej waluty z danego dnia?
#    2. W jakim formacie musi być data?
#    3. Co trzeba zmienić w URLu, aby otrzymać odpowiedź w JSONie zamiast XMLu?
# 2. Tabele kursów są publikowane tylko w dni robocze. Przeczytaj w dokumentacji co się stanie, gdy zapytasz o kurs z weekendu lub innego dnia wolnego od pracy?
# 3. Twój program przyjmuje walutę oraz datę jako dwa argumenty wiersza poleceń. Jeśli jednak nie zostaną podane, wówczas poproś użytkownika o podanie tych dwóch informacji przy pomocy funkcji input.
from datetime import datetime
from dateutil import parser
import sys
import requests
import glob
import os
import json
#URL = r'http://api.nbp.pl/api/exchangerates/rates/a/WALUTA/data/?format=json'
#https://api.nbp.pl/api/exchangerates/rates/a/gbp/2022-01-12/?format=json

WALUTA=None
DATA= None

DATE_FORMAT=("%Y-%m-%d")



URL = f'http://api.nbp.pl/api/exchangerates/rates/a/{WALUTA}/{DATA}/?format=json'
print(URL)
#file = requests.get(URL)
#a = file.json()
#print(file)
#print(a['rates'][0]['mid'])
##print(a['code'])

try:
    file = requests.get(URL)
    a = file.json()
    print(file)
    print(a['rates'][0]['mid'])
  
except json.JSONDecodeError:
    print('Brak kursu dla danego dnia!')
for sys_arg in sys.argv:
    file = requests.get(URL)
    a = file.json()
    if len(sys.argv)==3:
        waluta = sys.argv[1]
        kurs= a['rates'][0]['mid']
        data = sys.argv[2]
        data= parser.parse(DATA)
        data=data.date()
        print(f'kurs {waluta} na dzień {data} wynosi {kurs}')

    elif len(sys.argv)<3 and WALUTA ==None and DATA is not None:
        waluta =input('Podaj walute:')
        kurs= a['rates'][0]['mid']
        data = sys.argv[2]
        data= parser.parse(DATA)
        data=data.date()
        print(f'kurs {waluta} na dzień {data} wynosi {kurs}')

    elif len(sys.argv)<3 and WALUTA is not None and DATA is None:
        waluta = sys.argv[1]
        kurs= a['rates'][0]['mid']
        data = input('Podaj datę:')
        print(f'kurs {waluta} na dzień {data} wynosi {kurs}')

    else:
        print('Podano za dużo argumentów')