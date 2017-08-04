from func import *
import sys

def control(id):
	with db:
		for i in db.execute("SELECT * FROM users WHERE vkid=(?)", (id,)):
			for j in db.execute("SELECT * FROM discounts"):
				if (j[8] and ('1' in i[14])) or (j[9] and ('2' in i[14])):
					send(id, j[1]+'\nОбычная цена: '+str(j[2])+'\nЦена со скидкой в Steam: '+str(j[3])+' (-'+j[4]+str(round(100*(1-j[3]/j[2]), 2))+'%)\nhttp://store.steampowered.com/app/'+str(j[0]), ['photo-151313066_'+str(j[5])] if j[5] else Null)

if __name__=='__main__':
	control(int(sys.argv[1]))