from func import *
import sys

from ZakaZaka import ChangeNameToZakaZaka
from SteamPay import ChangeNameSP
from SteamBuy import ChangeNameSB

#Отправляем рекомендации пользователю
def control(id):
	with db:
		for i in db.execute("SELECT * FROM users WHERE vkid=(?)", (id,)):
			for j in db.execute("SELECT * FROM discounts WHERE active=1"):
				if (j[8] and ('1' in i[14])) or (j[9] and ('2' in i[14])):
					#+'\n'+j[5]
					text=j[1]+'\nОбычная цена: '+str(j[2])+'₽\n--------------------\nЦена со скидкой в Steam: '+str(j[3])+'₽ (-'+str(round(100*(1-j[3]/j[2]), 2))+'%)\nhttp://store.steampowered.com/app/'+str(j[0])
					if j[11]:
						text+='\n--------------------\nЦена в ZakaZaka: '+str(j[11])+'₽ (-'+str(round(100*(1-j[11]/j[2]), 2))+'%)\nhttps://zaka-zaka.com/game/'+ChangeNameToZakaZaka(j[1])
					if j[12]:
						text+='\n--------------------\nЦена в StemPay: '+str(j[12])+'₽ (-'+str(round(100*(1-j[12]/j[2]), 2))+'%)\nhttp://steampay.com/game/'+ChangeNameSP(j[1])
					if j[13]:
						text+='\n--------------------\nЦена в SteamBuy: '+str(j[13])+'₽ (-'+str(round(100*(1-j[13]/j[2]), 2))+'%)\nhttp://steambuy.com/steam/'+ChangeNameSB(j[1])

					send(id, text, ['photo-151313066_'+str(j[4])] if j[4] else [])

if __name__=='__main__':
	control(int(sys.argv[1]))