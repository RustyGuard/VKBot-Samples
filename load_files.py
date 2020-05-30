import vk_api

from secrets import LOGIN, PASSWORD


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    upload = vk_api.VkUpload(vk_session)

    files = []
    msg = input('Введите название файла(оставить пустым для прекращения)')
    while msg:
        files.append(msg)
        msg = input('Введите название файла(оставить пустым для прекращения)')
    album_id = input('Введите id альбома')
    group_id = input('Введите id группы')
    for file in files:
        upload.photo(file, album_id, group_id)


if __name__ == '__main__':
    main()
