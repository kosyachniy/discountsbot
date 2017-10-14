import requests
from bs4 import BeautifulSoup

url='https://steampay.com/search?q='

def SearchingSteamPay(name):
    page = requests.get(url+name).text
    soup = BeautifulSoup(page,'lxml')
    try:
        #print(soup)
        div = soup.find('div', class_ = 'catalog-item__price')
        price = div.find('span', class_ = 'catalog-item__price-span').next_element.strip()
        #print(price)
        href = soup.find('a',class_ = 'catalog-item').get('href')
        #print(href)
        finalhref = url+href
        print(finalhref)
        return price,finalhref
    except:
        return 0
SearchingSteamPay('g')

