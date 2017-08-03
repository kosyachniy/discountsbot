from func import *

char='йцукенгшщзхъёфывапролджэячсмитьбюqwertyuiopasdfghjklzxcvbnm1234567890'

mon={'понедельник', 'пн', 'пон', 'понед', 'monday', 'mon', 'mond'}
tue={'вторник', 'вт', 'вторн', 'tuesday', 'tue'}
wed={'среда', 'ср', 'сред', 'wednesday', 'wednes', 'wed'}
thu={'четверг', 'чт', 'четв', 'thursday', 'thu'}
fri={'пятница', 'пт', 'пятн', 'friday', 'fri'}
sat={'суббота', 'суб', 'суббот', 'субота', 'субот', 'saturday', 'sat'}
sun={'воскресенье', 'воск', 'воскрес', 'sunday', 'sun'}

win={'windows', 'win', 'виндоус', 'винда', 'pc', 'пк'}
mac={'macos', 'mac', 'мак', 'макос', 'макбук', 'macbook', '', '', ''}
ndr={'android', 'андроид', 'андрюша', 'самсунг', 'ксьоми', 'шяоми', 'мейзу', 'meizu', 'xiaomi', 'samsung'}
ios={'ios', 'iphone', 'ipad', 'ipod', 'apple', 'айос', 'айфон', 'эпл', 'айпад', 'айпод'}

def text(id, cont):
	cont=list(cont.lower())
	for i in range(len(cont)):
		if cont[i] not in char:
			cont[i]=' '
	text=''.join(cont).split()

	days=[]
	for i in text:
		if i in mon:
			days+=[1]
		elif i in tue:
			days+=[2]
		elif i in wed:
			days+=[3]
		elif i in thu:
			days+=[4]
		elif i in fri:
			days+=[5]
		elif i in sat:
			days+=[6]
		elif i in sun:
			days+=[7]
	if len(days):
		with db:
			days.sort()
			db.execute("UPDATE users SET days=(?) WHERE vkid=(?)", (','.join([str(i) for i in days]), id))
		return 1

	platform=[]
	for i in text:
		if i in win:
			platform+=[1]
		elif i in mac:
			platform+=[2]
		elif i in ndr:
			platform+=[3]
		elif i in ios:
			platform+=[4]
	if len(platform):
		with db:
			platform.sort()
			db.execute("UPDATE users SET platform=(?) WHERE vkid=(?)", (','.join([str(i) for i in platform]), id))
		return 2

while True:
	with db:
		for i in read():
			t=True
			for j in db.execute("SELECT * FROM users WHERE vkid=(?)", (i[0],)):
				indicator=text(*i)
				
				if not j[14] and indicator!=1:
					send(i[0], 'Какие платформы тебя интересуют?\nДоступные: iOS / Android / Windows / MacOS')
				elif not j[16] and indicator!=2:
					send(i[0], 'Любимые жанры?')

				t=False
				break

			if t:
				db.execute("INSERT INTO users (verified, name, surname, sex, birthday, photo, address, language, phone, timezone, home, vkid, vknick, platform, days, genre) VALUES ('%d', '%s', '%s', '%d', '%d', '%s', '%s', '%s', '%d', '%d', '%s', '%d', '%s', '', '', '')" % info(i[0]))
				send(i[0], 'Привет! Я тот, кто будет тебе говорить о самых интересных скидках в Steam, PlayMarket и AppStore!\nПо каким дням недели тебе можно писать?')
#То что ты захочешь и когда ты захочешь
			time.sleep(1)