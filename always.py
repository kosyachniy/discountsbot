from control import *
from discounts import update

#Отправка раз в день рекомендаций
while True:
	update()
	tim=time.gmtime()
	ti=tim.tm_hour*100+tim.tm_min
	for i in dial():
		with db:
			for j in db.execute("SELECT * FROM users WHERE vkid=(?)", (i,)):
				if 900 <= ti+j[10] < 1000:
					control(i)
	time.sleep(3600)