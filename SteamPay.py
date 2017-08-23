from bs4 import BeautifulSoup
import requests

url='http://steampay.com/game/'
def ChangeNameSB(name):
    name = name.replace(' ','-')
    name = name.replace(':','-')
    name = name.replace('.','-')
    name = name.lower()
#    print(name)
    return(name)

def GetPriceFromSP(name):
    name = ChangeNameSB(name)
    page = requests.get(url+name).text
    soup = BeautifulSoup(page, 'lxml')
    price = soup.find('span',class_="price").next_element
    #print(scan)
    #price = scan.next_elemnt()
#    print(price)
    return(price)

GetPriceFromSP('Get even')

