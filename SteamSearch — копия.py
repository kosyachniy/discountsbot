from bs4 import BeautifulSoup
import requests

url = 'http://store.steampowered.com/search/?term='

def ResultOfSearch(name):
    page = requests.get(url+name).text
    soup = BeautifulSoup(page , 'lxml')
    div = soup.find('div', id = 'search_result_container')
    #print(div)
    #return div
    a = div.find('a')
    href = a.get('href')
    #print(href)
    page = requests.get(href).text
    soup = BeautifulSoup(page,'lxml')
    div = soup.find('div', class_ = 'game_purchase_price price')
    #print(div)
    if (div == None):
        div = soup.find('div', class_='discount_final_price').next_element
    else:
        div = div.next_element.strip()
    div = div[:-5]
    print(href)
    print(div)
    return div,href

ResultOfSearch('rocket')