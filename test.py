from func import *

values = {'album_id': '247231511', 'group_id': '151313066'}
url=vk.method('photos.getMessagesUploadServer', values)['upload_url']
photo=open('1.jpg','rb')
print(vk.http.post(url, files=photo))
#response = json.loads(str())
#vk.method('photos.save', response)