import requests, time, json, sqlite3, vk_api
from bs4 import BeautifulSoup
from urllib.request import unquote
from parse import parse

def text(x):
	y=[]
	for i in parse(x):
		for j in i.word:
			if j['speech']!='sign':
				y.append(j['infinitive'])
	return y

with open('set.txt', 'r') as file:
	s=json.loads(file.read())
	vk=s['vk']
	steam=s['steam']

names=lambda name: unquote(name[name.rfind('/')+1:])

#VK
vk=vk_api.VkApi(token=vk)
vk.auth()

send=lambda user, cont, img=[]: vk.method('messages.send', {'user_id':user, 'message':cont, 'attachment':','.join(img)})

def read():
	cont=[]
	for i in vk.method('messages.get')['items']:
		if not i['read_state']:
			cont.append([i['user_id'], i['body']])
	return cont[::-1]

def info(user):
	x=vk.method('users.get', {'user_ids': user, 'fields': 'verified, first_name, last_name, sex, bdate, photo_id, country, city, lang, phone, timezone, home_town, screen_name'})[0]

	bd=x['bdate']
	if bd.count('.')==2:
		bd=time.strftime('%Y%m%d', time.strptime(bd, '%d.%m.%Y'))
	else:
		bd=time.strftime('%m%d', time.strptime(bd, '%d.%m'))

	return (x['verified'], x['first_name'], x['last_name'], x['sex'], int(bd), x['photo_id'], str(x['country']['id'])+'/'+str(x['city']['id']), 0, 0, 3, 0, user, x['screen_name'])

#SQLite
db=sqlite3.connect('main.db')

'''
#Steam
from steam import WebAPI, SteamClient

api=WebAPI(key=steam)
'''