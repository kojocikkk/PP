# Pomóż szwajcarskiemu bankowi HSBC tworząc aplikację, która odczytuje i analizuje dane z Narodowego Banku Polskiego (NBP) udostępnione przez API i podaje ile była warta wskazana waluta we wskazanym dniu.

# Dzięki Tobie HSBC będzie mógł poprawnie wystawiać w Polsce faktury w walucie obcej - przepisy wymagają, aby kwoty na takich fakturach przeliczać na złotówki wg kursów NBP z określonych dni.

# 1. Zapoznaj się z opisem API: http://api.nbp.pl.
#    1. Ustal jak wygląda URL, pod którym znajdziesz kurs danej waluty z danego dnia?
#    2. W jakim formacie musi być data?
#    3. Co trzeba zmienić w URLu, aby otrzymać odpowiedź w JSONie zamiast XMLu?
# 2. Tabele kursów są publikowane tylko w dni robocze. Przeczytaj w dokumentacji co się stanie, gdy zapytasz o kurs z weekendu lub innego dnia wolnego od pracy?
# 3. Twój program przyjmuje walutę oraz datę jako dwa argumenty wiersza poleceń. Jeśli jednak nie zostaną podane, wówczas poproś użytkownika o podanie tych dwóch informacji przy pomocy funkcji input.
from datetime import datetime
from msilib.schema import Error
from dateutil import parser
import sys
import requests
import glob
import os
import json
#URL = r'http://api.nbp.pl/api/exchangerates/rates/a/WALUTA/data/?format=json'
#https://api.nbp.pl/api/exchangerates/rates/a/gbp/2022-01-12/?format=json

waluta= None
data= None
i=0
tabela_walut =f'http://api.nbp.pl/api/exchangerates/tables/a/'
try:
    file = requests.get(tabela_walut)
    b = file.json()
except json.JSONDecodeError:
    print(' brak kursów walut')

kod =None
kody_walut=[]
for item in b:
    item =b[0]['rates']
    #print(item)
    for item2  in item:
        for item3 in item2.values():
            if len(str(item3)):
                kody_walut.append(item3) 
        
    i=+1
    print(kody_walut)

try:
    len(sys.argv[1]) ==3
    waluta = sys.argv[1]
        
except:
    ValueError('Podałeś błedną walutę!')
    waluta=input("Podaj prawidłową walutę: ")

waluta= waluta.upper()   

try:
    data=sys.argv[2]     
except:
    ValueError('Brak daty!')
    data=input("Podaj datę: ")

data= parser.parse(data)
data=data.date()

URL = f'http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{data}/?format=json'

print(URL)
try:
    file = requests.get(URL)
    a = file.json()
    
    kurs=(a['rates'][0]['mid'])
    print(f'kurs {waluta} na dzień {data} wynosi {kurs}')
except json.JSONDecodeError:
    print('Brak kursu dla danego dnia!')

