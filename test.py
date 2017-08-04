from func import *

group=151313066
album=247214009
photo=open('1.jpg', 'rb')
values={'group_id': 151313066, 'album_id': 247214009}

a=vk.method('photos.getMessagesUploadServer', values) #, {'group_id': group, 'album_id': album, 'photo': {'photo': photo}}
print(a)

'''
response=requests.post(a['upload_url'], files=dict(foo=photo))
print(response.status_code)

from pprint import pprint
pprint(response.json()) #['headers']

e=vk.http.post(a['upload_url'], files={'photo': photo})
print(e)
'''


b=requests.get(a['upload_url']).text
print(b)

c=json.loads(b)
print(c)

d=vk.method('photos.saveMessagesPhoto', {'photo': {'photo': photo}, 'server': c['server'], 'hash': c['hash']})
print(d)