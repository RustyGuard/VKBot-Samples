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
    vk = vk_session.get_api()
    response = vk.friends.get(fields="bdate, city")
    if response['items']:
        for i in sorted(response['items'], key=lambda x: x['last_name']):
            print(i['last_name'], i['first_name'], i.get('bdate', 'Не получено'))


if __name__ == '__main__':
    main()
