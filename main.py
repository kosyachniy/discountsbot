from func import *

mon={'понедельник', 'пн', 'пон', 'понед', 'monday', 'mon', 'mond'}
tue={'вторник', 'вт', 'вторн', 'tuesday', 'tue'}
mon={'среда', '', '', '', '', '', '' 'пон', 'monday', 'mon'}
mon={'понедельник', 'пон', 'monday', 'mon'}
mon={'понедельник', 'пон', 'monday', 'mon'}
mon={'понедельник', 'пон', 'monday', 'mon'}
mon={'понедельник', 'пон', 'monday', 'mon'}

while True:
	with db:
		for i in read():
			t=True
			for i in db.execute("SELECT * FROM users WHERE vkid=(?)", (i[0],)):
				
				t=False
				break

			if t:
				db.execute("INSERT INTO users (verified, name, surname, sex, birthday, photo, address, language, phone, timezone, home, vkid, vknick, platform, frequency, genre) VALUES ('%d', '%s', '%s', '%d', '%d', '%s', '%s', '%s', '%d', '%d', '%s', '%d', '%s', '', '', '')" % info(i[0]))
				send(i[0], 'Привет! Я тот, кто будет тебе говорить о самых интересных скидках в Steam, PlayMarket и AppStore!\nПо каким дням недели тебе можно писать?')
#То что ты захочешь и когда ты захочешь
			time.sleep(1)