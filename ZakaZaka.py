import requests
from bs4 import BeautifulSoup


url='https://zaka-zaka.com/game/'
def ChangeNameToZakaZaka(name):
        name = name.replace(' ', '-')
        name = name.replace(':', '-')
        name = name.replace('.','-')
        name = name.lower()
#        print(name)
        return name
    
def GetPriceFromZakaZaka(name):
    name = ChangeNameToZakaZaka(name)
    page = requests.get(url+name).text
    soup = BeautifulSoup(page, 'lxml')
    scan = soup.find('p',itemprop="price")
#price = scan.find('content')
    price = scan.get('content')
#    print(price)
    return price

#GetPriceFromZakaZaka('Alan Wake')
