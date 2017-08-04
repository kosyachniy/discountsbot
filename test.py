from func import *

group=151313066
album=247214009
photo=open('1.jpg', 'rb')

a=vk.method('photos.getMessagesUploadServer', {'group_id': group, 'album_id': album, 'photo': ('1.jpg', photo)})
print(a)

b=requests.get(a['upload_url']).text
print(b)

c=json.loads(b)
print(c)

d=vk.method('photos.saveMessagesPhoto', {'photo': ('1.jpg', photo), 'server': c['server'], 'hash': c['hash']})
print(d)