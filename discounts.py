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

def update():
	with db: db.execute("DELETE FROM discounts")

#Парсим страницу скидок
	result=soup.find_all('a', class_='search_result_row')
	for i in result:
		id=int(i.get('data-ds-appid'))
		name=i.find('span', class_='title').text
		price=i.find('div', class_='search_price').contents
		original=num(price[1].text)
		steam=num(price[3])
		win=1 if i.find('span', class_='win') else 0
		mac=1 if i.find('span', class_='mac') else 0

#Считываем описание
		#Сделать русский язык
		try:
			pag=requests.get('http://store.steampowered.com/app/'+str(id), data={'Accept-Language': 'RU'}).text
			sp=BeautifulSoup(pag, 'lxml') #, 'html5lib')
			desc=sp.find('div', class_='game_description_snippet').contents[0].strip()
		except:
			print('Error!')
			desc=''

#Загружаем изображение на сервер
		out=open('main.jpg', 'wb')
		out.write(requests.get('http://cdn.akamai.steamstatic.com/steam/apps/'+str(id)+'/header.jpg').content)
		out.close()

#Загружаем изображение в ВК
		with open('set.txt', 'r') as file:
			s=json.loads(file.read())
			vks=vk_api.VkApi(s['login'], s['pass'])
			vks.auth()
			upload=vk_api.VkUpload(vks)
			photo=upload.photo('main.jpg', album_id=247231511, group_id=151313066)
			print('photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id']))

#Вносим в БД
		print(id, name, original, steam, win, mac)
		with db: db.execute("INSERT INTO discounts VALUES (?, ?, ?, ?, ?, ?, 0, 0, ?, ?)", (id, name, original, steam, photo[0]['id'], desc, win, mac))

if __name__=='__main__':
	update()