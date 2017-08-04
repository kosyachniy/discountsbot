from func mport *

values = {}

        if user_id:
            values['user_id'] = user_id
        elif group_id:
            values['group_id'] = group_id

        response = self.vk.method('photos.getWallUploadServer', values)
        url = response['upload_url']

        photos_files = open_files(photos)
        response = self.vk.http.post(url, files=photos_files)
        close_files(photos_files)

        values.update(response.json())

        response = self.vk.method('photos.saveWallPhoto', values)

        return response