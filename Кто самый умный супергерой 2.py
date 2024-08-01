import requests


def get_the_smartest_superhero(superheros):
    the_smartest_superhero = ''
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'  # ссылка на api
    response = requests.get(url)  # отправляем запрос
    if 200 <= response.status_code < 300:  # если запрос прошел успешно
        data = response.json()  # получаем данные
        intelligence_list = []  # создаем список с интелектом
        for hero in data:  # проходимся по списку
            if hero['id'] in superheros:  # если id супергероя в списке
                intelligence_list.append(
                    {'name': hero['name'], 'intelligence': hero['powerstats']['intelligence']})  # Add name to the list
        intelligence_list.sort(key=lambda x: x['intelligence'], reverse=True)  # сортируем список по убыванию интеллекта
        the_smartest_superhero = intelligence_list[0]['name']  # получаем имя супергероя с самым высоким интелектом
    return the_smartest_superhero


print(get_the_smartest_superhero([1, 22, 5]))
