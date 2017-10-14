import requests
from bs4 import BeautifulSoup

url='http://steampay.com/search.php?q='

def SearchingSteamPay(name):
    page = requests.get(url+name.replace(' ', '+')).text
    soup = BeautifulSoup(page,'lxml')
    print(page)
    div = soup.find('div', class_ = 'list_products')
    a = div.find('a')
    href = a.get('href')
    finalhref = 'http://steampay.com'+href #конечная ссылка которая будет возвращаться
    price = a.find('span', class_='cost').next_element #поиск цены, если возвращается - то данной игры нет в наличии
    print(price)
    return price,finalhref

SearchingSteamPay('Quantum Break')