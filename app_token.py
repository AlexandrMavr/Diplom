import vk_api
from vk_api.longpoll import VkLongPoll
from config import app_token

vk_app = vk_api.VkApi(token=app_token)
session_api_user = vk_app.get_api()
longpoll_user = VkLongPoll(vk_app)

def info_user(user_id):
    info_user = vk_app.method('users.get', {'users_ids': user_id, 'fields': 'last_name, city, sex, bdate, relation'})
    return info_user

def parametrs_candidates(offset, id_city, search_sex, birth_year):
    parametrs_can = vk_app.method('users.search',
                                  {'count': 1, 'sort': 0, 'offset': offset, "city": id_city, "sex": search_sex, 'birth_year': birth_year, 'has_photo': 1, 'relation': 6})
    return parametrs_can

def photo_candidates_sort(user_id):
    photo_candidates = vk_app.method('photos.getAll', {'owner_id': user_id, 'extended': 1, 'count': 200})
    list_photo_c = {}
    for i in photo_candidates.get("items"):
        x = i.get("likes")
        y = x.get("count")
        z = i.get("id")
        list_photo_c[f'photo{user_id}_{z}'] = y
        photo_candidates_sort = sorted(list_photo_c.items(), key=lambda x: x[1])
    return photo_candidates_sort

