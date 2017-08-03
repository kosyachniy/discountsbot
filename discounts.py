from func import *

page=requests.get('http://store.steampowered.com/search/?specials=1').text
soup=BeautifulSoup(page, 'lxml') #, 'html5lib')

def num(text):
	cont=''
	for i in text:
		if i.isdigit():
			cont+=i
		elif i==',':
			cont+='.'
	return float(cont)

result=soup.find_all('a', class_='search_result_row')
for i in result:
	id=int(i.get('data-ds-appid'))
	name=i.find('span', class_='title').text
	price=i.find('div', class_='search_price').contents
	original=num(price[1].text)
	steam=num(price[3])
	win=1 if i.find('span', class_='win') else 0
	mac=1 if i.find('span', class_='mac') else 0

	print(id, name, original, steam, win, mac)
	with db: db.execute("INSERT INTO discounts VALUES (%d, '%s', %f, %f, '%s', 0, 0, %d, %d)" % (id, name, original, steam, '', win, mac))