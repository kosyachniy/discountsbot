from bs4 import BeautifulSoup
import requests

url = 'https://zaka-zaka.com/search/?game='

def AdditionalZakaZakaSearch(name):
    page = requests.get(url+name).text
    soup = BeautifulSoup(page,'lxml')
    price = soup.find('p').next_element
  
    li = soup.find('li', class_ = "odd")
    name = li.find('h1').next_element.next_element
    href = li.find('a').get('href')
    
    #print(price)
    #print(name)
    #print(href)
    return url+href,price

#print(AdditionalZakaZakaSearch('f')[0])
