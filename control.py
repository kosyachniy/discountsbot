from func import *

def control(id):
	with db:
		for i in db.execute("SELECT * FROM users WHERE vkid=(?)", (id,)):
			for j in db.execute("SELECT * FROM discounts"):
				if (j[7] and (1 in i[14])) or (j[8] and (2 in i[14])):
					send(id, j[1]+'\nОбычная цена: '+str(j[2])+'\nЦена со скидкой в Steam: '+str(j[3])+'\n'+j[4]+str(round(100*(1-j[4]/j[3]), 2)))