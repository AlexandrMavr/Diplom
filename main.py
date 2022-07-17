import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
from app_token import info_user
from app_token import parametrs_candidates
from app_token import photo_candidates_sort
import Data_base_vk
from config import password, database, user, host, port, community_token

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': 0})

def send_photo(user_id, message, photo):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'attachment': photo,  'random_id': 0})

if __name__ == '__main__':

    vk = vk_api.VkApi(token=community_token)
    session_api = vk.get_api()
    longpoll = VkLongPoll(vk)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:
                request = event.text

                if request == "привет":
                    write_msg(event.user_id, f"Хай, {event.user_id}")

                elif request == "найди мне пару":
                    x = info_user(event.user_id)
                    offset = randint(1, 200)
                    id_city = x[0]['city']['id']
                    search_sex = 1 if x[0]['sex'] == 2 else 2
                    birth_year = x[0]['bdate'][-4:]
                    z = parametrs_candidates(offset, id_city, search_sex, birth_year)
                    if z['items'] == []:
                        write_msg(event.user_id, "Что-то идет не так\n"
                                                 "Давай еще раз!\n")
                    else:
                        write_msg(event.user_id, "Смотри кого нашел\n")
                        d = z['items'][0]["is_closed"]
                        a = z['items'][0]['first_name']
                        b = z['items'][0]['last_name']
                        c = z['items'][0]['id']
                        str_response = f"INSERT INTO CANDIDATES1 (first_name, last_name, vk_id_user) VALUES (\'{a}\', \'{b}\', \'{c}\')"
                        candidat = Data_base_vk.CandidatInBase(database, user, password, host, port, str_response)
                        candidat.insert_bd_candadets(str_response)
                        candidat.close_bd()
                        write_msg(event.user_id, "Вот она твоя мечта или нет?"
                                                 f"https://vk.com/id{c}")

                        if d == True:
                            write_msg(event.user_id, "Но аккуант приватный, фотки не увидим\n"
                                                    "Давай попробуем еще раз?\n")
                        elif len(photo_candidates_sort(c)) < 3:
                            write_msg(event.user_id, "Фото маловато не оценить\n"
                                                     "Давай попробуем еще раз?\n")
                        else:
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
