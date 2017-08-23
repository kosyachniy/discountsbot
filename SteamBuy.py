from bs4 import BeautifulSoup
import requests

url='http://steambuy.com/steam/'
def ChangeNameSB(name):
    name = name.replace(' ','-')
    name = name.replace(':','-')
    name = name.replace('.','-')
    name = name.lower()
#    print(name)
    return(name)

def GetPriceFromSB(name):
    name = ChangeNameSB(name)
    page = requests.get(url+name).text
    soup = BeautifulSoup(page, 'lxml')
    price = soup.find('span',class_="tovar-price").next_element
    #print(scan)
    #price = scan.next_elemnt()
#    print(price)
    return(price)

GetPriceFromSB('Football manager 2017')
