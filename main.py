import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
from user_token import info_user
from user_token import parametrs_candidates
from user_token import photo_candidates_sort
from Data_base_vk import insert_bd_candadets
from Data_base_vk import close_bd
from parol_and_tokens import community_token


vk = vk_api.VkApi(token=community_token)
session_api = vk.get_api()
longpoll = VkLongPoll(vk)

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': 0})

def send_photo(user_id, message, photo):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'attachment': photo,  'random_id': 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            if request == "привет":
                write_msg(event.user_id, f"Хай, {event.user_id}")

            elif request == "найди мне пару":
                write_msg(event.user_id, "Смотри кого нашел\n")
                x = info_user(event.user_id)
                offset = randint(1, 100)
                id_city = x[0]['city']['id']
                search_sex = 1 if x[0]['sex'] == 2 else 2
                birth_year = x[0]['bdate'][-4:]
                z = parametrs_candidates(offset, id_city, search_sex, birth_year)
                a = z['items'][0]['first_name']
                b = z['items'][0]['last_name']
                c = z['items'][0]['id']
                str_response = f"INSERT INTO CANDIDATES1 (first_name, last_name, vk_id_user) VALUES (\'{a}\', \'{b}\', \'{c}\')"
                insert_bd_candadets(str_response)
                close_bd()
                write_msg(event.user_id, "Вот она твоя мечта или нет?"
                                         f"https://vk.com/id{c}")
                send_photo(event.user_id, 'Смотри какая фоточка', photo_candidates_sort(c)[-1][0])
                send_photo(event.user_id, 'Еще одна', photo_candidates_sort(c)[-2][0])
                send_photo(event.user_id, 'И еще', photo_candidates_sort(c)[-3][0])

            elif request == "пока":
                write_msg(event.user_id, "Пока((")

            else:
                write_msg(event.user_id, "Не понял вас ... Можно попроще\n"
                                         "Напиши: найди мне пару\n"
                                         "Или напиши: пока\n"
                                         "Или напиши: привет\n"
                                         "Будь проще и люди потянуться к тебе и боты тоже\n")
