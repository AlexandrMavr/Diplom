import vk_api
from vk_api.longpoll import VkLongPoll


app_token = 'vk1.a.uTuhFM1sPVdVvllBHk26AU8uTdUr84PWyCqYEq4JU6xfga8biNKFX02dy8fNDypMolWrnQTbcZAK9Y9d1zegkhctCBtR9Z1VZ_05Kbac_RkMR9JvLlHeaXE2tdVJeq2g_tMj8mrwmCdOc7NAQqEyWlSGbgYD8pBk55c8cHmHEyYVBbGzoPg2AOgPYz14rqRg'
vk_user = vk_api.VkApi(token=app_token)
session_api_user = vk_user.get_api()
longpoll_user = VkLongPoll(vk_user)

def info_user(user_id):
    info_user = vk_user.method('users.get', {'users_ids': user_id, 'fields': 'last_name, city, sex, bdate, relation'})
    return info_user
    # print(info_user)
    # print(info_user[0])

    # id_city = info_user[0]['city']['id']
    # search_sex = 1 if info_user[0]['sex'] == 2 else 2
    # relation_search = 6
    # birth_year = info_user[0]['bdate'][-4:]
    # # offset = 1

def parametrs_candidates(offset, id_city, search_sex, birth_year):
    parametrs_can = vk_user.method('users.search',
    {'count': 1, 'sort': 0, 'offset': offset, "city": id_city, "sex": search_sex, 'birth_year': birth_year, 'has_photo': 1, 'relation': 6})
    return parametrs_can

    # x1 = parametrs_can['items'][0]['first_name']
    # x2 = parametrs_can['items'][0]['last_name']
    # x3 = parametrs_can['items'][0]['id']
    #
    # str_response = f"INSERT INTO CANDIDATES1 (first_name, last_name, vk_id_user) VALUES (\'{x1}\', \'{x2}\', \'{x3}\')"
    # # print(parametrs_can['count'])
    # # print(x1, x2, x3)


def photo_candidates_sort(user_id):
    photo_candidates = vk_user.method('photos.getAll', {'owner_id': user_id, 'extended': 1, 'count': 200})
    list_photo_c = {}
    for i in photo_candidates.items():
        if i[0] == "items":
            for y in i[1]:
                for k in y.items():
                    if k[0] == "likes":
                        list_photo_c[f'photo{user_id}_{y["id"]}'] = k[1]["count"]

    photo_candidates_sort = sorted(list_photo_c.items(), key=lambda x: x[1])
    return photo_candidates_sort

    # x1 = list_photo_c_sort[-1]
    # x2 = list_photo_c_sort[-2]
    # x3 = list_photo_c_sort[-3]
