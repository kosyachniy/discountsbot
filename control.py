from func import *

def control(id):
	with db:
		for i in db.execute("SELECT * FROM users WHERE vkid=(?)", (id,)):
			for j in db.execute("SELECT * FROM discounts"):
				if (j[7] and ('1' in i[14])) or (j[8] and ('2' in i[14])):
					values = {'album_id': '247231511', 'group_id': '151313066'}
					url=vk.method('photos.getMessagesUploadServer', values)['upload_url']
					photo=open('1.jpg','rb')
					response = json.loads(vk.http.post(url, files=photo))
					vk.method('photos.save', values)

					send(id, j[1]+'\nОбычная цена: '+str(j[2])+'\nЦена со скидкой в Steam: '+str(j[3])+' (-'+j[4]+str(round(100*(1-j[3]/j[2]), 2))+'%)\nhttp://store.steampowered.com/app/'+str(j[0]))