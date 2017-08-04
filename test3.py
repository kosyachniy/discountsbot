from func import *
import requests


values={'group_id':151313066, 'album_id':247231511}

response=vk.method('photos.getMessagesUploadServer', values)
#response['photo']=open('1.jpg','rb')
r=json.dumps(response)
#print(response)
#vk.http.post(response['upload_url'], files=open('1.jpg','rb'))
#response['server']=840123
#response['hash']='1fab5c4e6399f7b0722770ee4e4a58d8'
print(response)
'''
photo=open('1.jpg','rb')
one=vk.method('photos.getMessagesUploadServer')
print(one)
l=requests.get(one['upload_url']).text
r=json.loads(l)
print(r)
r['photo']='http://cdn.akamai.steamstatic.com/steam/apps/367520/header.jpg?t=1501775233' #photo
r=json.dumps(r)
print(r)
'''

#print(vk.method('photos.saveMessagesPhoto', {'photo':photo, 'server':r['server'], 'hash':r['hash'], 'group_id':one['group_id'], 'album_id':one['album_id']}))
print(vk.method('photos.saveMessagesPhoto', {'photo':r}))