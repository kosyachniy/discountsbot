from control import *

char='йцукенгшщзхъёфывапролджэячсмитьбюqwertyuiopasdfghjklzxcvbnm1234567890'

mon={'понедельник', 'понедельникам', 'понедельники', 'пн', 'пон', 'понед', 'monday', 'mon', 'mond'}
tue={'вторник', 'вторникам', 'вторники', 'вт', 'вторн', 'tuesday', 'tue'}
wed={'среда', 'средам', 'среды', 'ср', 'сред', 'wednesday', 'wednes', 'wed'}
thu={'четверг', 'четвергам', 'четверги', 'чт', 'четв', 'thursday', 'thu'}
fri={'пятница', 'пятницам', 'пятницы', 'пт', 'пятн', 'friday', 'fri'}
sat={'суббота', 'субботам', 'субботы', 'суботам', 'суб', 'суббот', 'субота', 'субот', 'saturday', 'sat'}
sun={'воскресенье', 'воскресеньям', 'воскресенья', 'воск', 'вск', 'вс', 'воскрес', 'sunday', 'sun'}

win={'windows', 'win', 'виндоус', 'виндовс', 'винда', 'pc', 'пк'}
mac={'macos', 'mac', 'мак', 'макос', 'макбук', 'macbook', '', '', ''}
ndr={'android', 'андроид', 'андрюша', 'самсунг', 'ксьоми', 'шяоми', 'мейзу', 'meizu', 'xiaomi', 'samsung'}
ios={'ios', 'iphone', 'ipad', 'ipod', 'apple', 'айос', 'айфон', 'эпл', 'айпад', 'айпод'}

act={'экшн', 'action', 'действие', 'экшен', 'экшены', 'actions', 'шутеры', 'шутер', 'shoot', 'shoots', 'fight', 'fights', 'файтинг', 'файхт', 'файтинги', 'аркада', 'аркады', 'боевик', 'боевики'}
sim={'симулятор', 'simulator', 'симмулятор', 'симуляторы', 'симмуляторы', 'simulators', 'спортивные', 'спорт', 'sport'}
tra={'стратегия', 'strategy', 'фермы', 'ферма', 'стратегии', 'варгейм', 'цивилизация', 'пошаговые', 'пошаговая', 'карточные', 'карточная', 'карты', 'civilization', 'carts'}
adv={'приключения', 'adventure', 'приключение', 'adventures', 'квест', 'квесты', 'quest'}
mus={'музыкальные', 'music', 'музыка', 'музыкальная', 'musics', 'ритм', 'ритмические'}
rol={'ролевые', 'role', 'ролевая', 'рпг', 'тактические', 'rpg', 'тактика'}
puz={'головоломки', 'puzzles', 'логические', 'логическая', 'логика', 'пазлы'}
des={'настольные', 'desktop', 'настольная', 'desktops', 'традиционные', 'традиционная'}
tex={'текстовые', 'text', 'texts', 'текстовая', 'псевдографика'}

#Определяем тип содержимого сообщения
def text(id, cont):
	cont=list(cont.lower())
	for i in range(len(cont)):
		if cont[i] not in char:
			cont[i]=' '
	text=''.join(cont).split()

#Дни недели
	days=set()
	for i in text:
		if i in mon:
			days.add(1)
		elif i in tue:
			days.add(2)
		elif i in wed:
			days.add(3)
		elif i in thu:
			days.add(4)
		elif i in fri:
			days.add(5)
		elif i in sat:
			days.add(6)
		elif i in sun:
			days.add(7)
	if len(days):
		with db:
			days=list(days)
			days.sort()
			db.execute("UPDATE users SET days=(?) WHERE vkid=(?)", (','.join([str(i) for i in days]), id))
		send(id, 'Установлены дни недели!')
		return 1

#Платформы
	platform=set()
	for i in text:
		if i in win:
			platform.add(1)
		elif i in mac:
			platform.add(2)
		elif i in ndr:
			platform.add(3)
		elif i in ios:
			platform.add(4)
	if len(platform):
		with db:
			platform=list(platform)
			platform.sort()
			db.execute("UPDATE users SET platform=(?) WHERE vkid=(?)", (','.join([str(i) for i in platform]), id))
		send(id, 'Установлены платформы!')
		return 2

#Жанры
	genres=set()
	for i in text:
		if i in act:
			genres.add(1)
		elif i in sim:
			genres.add(2)
		elif i in tra:
			genres.add(3)
		elif i in adv:
			genres.add(4)
		elif i in mus:
			genres.add(5)
		elif i in rol:
			genres.add(6)
		elif i in puz:
			genres.add(7)
		elif i in des:
			genres.add(8)
		elif i in tex:
			genres.add(9)
	if len(genres):
		with db:
			genres=list(genres)
			genres.sort()
			db.execute("UPDATE users SET genre=(?) WHERE vkid=(?)", (','.join([str(i) for i in genres]), id))
		send(id, 'Установлены жанры!')
		return 3

#Другое
	return 0

while True:
	with db:
		try:
			for i in read():
				t=0

#Если пользователь уже есть в БД, но не настроен
				for j in db.execute("SELECT * FROM users WHERE vkid=(?)", (i[0],)):
					indicator=text(*i)
					
					t=1
					if not j[15] and indicator!=1:
						send(i[0], 'По каким дням недели тебе можно писать?')
					elif not j[14] and indicator!=2:
						send(i[0], 'Какие платформы тебя интересуют?\nДоступные: Windows / MacOS') #iOS / Android / 
					elif not j[16] and indicator!=3:
						send(i[0], 'Любимые жанры?')
					else:
						t=2

#Если это новый пользователь
				if t==0:
					db.execute("INSERT INTO users (verified, name, surname, sex, birthday, photo, address, language, phone, timezone, home, vkid, vknick, platform, days, genre) VALUES ('%d', '%s', '%s', '%d', '%d', '%s', '%s', '%s', '%d', '%d', '%s', '%d', '%s', '', '', '')" % info(i[0]))
					send(i[0], 'Привет! Я тот, кто будет тебе говорить о самых интересных скидках в Steam!\nПо каким дням недели тебе можно писать?') #, PlayMarket и AppStore

#Если пользователь есть в БД и настроен
				elif t==2:
					control(i[0])

				time.sleep(1) #
		except vk_api.exceptions.ApiHttpError:
			vk.auth()
			print('Error!')
	time.sleep(1)