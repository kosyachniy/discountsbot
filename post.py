from func import *

while True:
	tim = time.gmtime().tm_hour + 3
	if 23 <= tim <= 24:
		num = 0
		for j in db.execute("SELECT * FROM discounts WHERE active=1"):
			num += 1
			if num == 9:
				break

			text=j[1]+'\nОбычная цена: '+str(j[2])+'₽\n--------------------\nЦена со скидкой в Steam: '+str(j[3])+'₽ (-'+str(round(100*(1-j[3]/j[2]), 2))+'%)\nhttp://store.steampowered.com/app/'+str(j[0])
			if j[11]:
				text+='\n--------------------\nЦена в ZakaZaka: '+str(j[11])+'₽ (-'+str(round(100*(1-j[11]/j[2]), 2))+'%)\nhttps://zaka-zaka.com/game/'+ChangeNameToZakaZaka(j[1])
			if j[12]:
				text+='\n--------------------\nЦена в StemPay: '+str(j[12])+'₽ (-'+str(round(100*(1-j[12]/j[2]), 2))+'%)\nhttp://steampay.com/game/'+ChangeNameSP(j[1])
			if j[13]:
				text+='\n--------------------\nЦена в SteamBuy: '+str(j[13])+'₽ (-'+str(round(100*(1-j[13]/j[2]), 2))+'%)\nhttp://steambuy.com/steam/'+ChangeNameSB(j[1])

			print(vks.method('wall.post', {'owner_id': -151313066, 'message': text, 'attachment': 'photo-151313066_' + j[4]}))

			time.sleep(7200)
	time.sleep(3600)