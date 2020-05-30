from datetime import datetime

import pytz
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random

from secrets import TOKEN


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, '193812050')
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk = vk_session.get_api()
            response = vk.users.get(user_id=event.obj.message['from_id'])[0]
            msg_text = event.obj.message['text'].lower()
            if any(i in msg_text for i in ['время', 'число', 'дата', 'день']):
                moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
                message = f'Сегодня {moscow_time.strftime("%x")}\n' \
                          f'Время в Москве {moscow_time.strftime("%T")}\n' \
                          f'День недели {moscow_time.strftime("%A")}'
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=message,
                                 random_id=random.randint(0, 2 ** 64))
            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message='Ну вот, а я бы тебе время сказал',
                                 random_id=random.randint(0, 2 ** 64))
            print('response', response)


if __name__ == '__main__':
    main()
