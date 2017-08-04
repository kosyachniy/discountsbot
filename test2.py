from func import *
import requests

values={'group_id':151313066, 'album_id':247231511}

response=vk.method('photos.getMessagesUploadServer', values)
#response['photo']=open('1.jpg','rb')
#vk.http.post(response['upload_url'], files=open('1.jpg','rb'))
#response['server']=840123
#response['hash']='1fab5c4e6399f7b0722770ee4e4a58d8'
print(response)

r=requests.get(vk.method('photos.getMessagesUploadServer')).text
print(r)

print(vk.method('photos.saveMessagesPhoto', {'photo':open('1.jpg','rb')}))