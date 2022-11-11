#Below code witch is checking the currency code from NBP website.
#The code also check currency code- also with NBP website.

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
    for item2 in item:
        for item3 in item2.items():
            if item3[0]=="code":
                kody_walut.append(item3[1])
                   
            i=+1
#print(kody_walut)

try:
    len(sys.argv[1]) ==3
    waluta = sys.argv[1]
    while waluta not in kody_walut:
        print(f'Podałeś błedną walutę! Nie ma takiej waluty jak {waluta} wybierz jedną z walut :\n {kody_walut}')
        waluta=input("Podaj prawidłową walutę: ")

except:
    ValueError('Nie podałeś waluty!')
    waluta=input("Nie podałeś waluty. Podaj prawidłową walutę: ")
    while waluta not in kody_walut:
        print(f'Podałeś błedną walutę! Nie ma takiej waluty jak {waluta} wybierz jedną z walut :\n {kody_walut}')

waluta= waluta.upper()   


try:
    data=sys.argv[2]     
except:
    ValueError('Brak daty!')
    data=input("Podaj datę: ")

try:
    data= parser.parse(data)
    data=data.date()
except:
    ValueError('Błedna data')


URL = f'http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{data}/?format=json'

print(URL)
try:
    file = requests.get(URL)
    a = file.json()
    
    kurs=(a['rates'][0]['mid'])
    print(f'kurs {waluta} na dzień {data} wynosi {kurs}')
    
except json.JSONDecodeError:
    print('Brak kursu dla danego dnia!')
