import requests
import json
from pprint import pprint

# url_anketa = "https://functions.yandexcloud.net/d4e8qsrmeednndemfsus"
# payload = {
#     "name": "Тимур",
#     "surname": "Тимур",
#     "patronymic": "Тимур",
#     "telephone": "+7(111)111-11-11",
#     "birthdate": "1111-11-11",
#     "passport": "1111 11111111"
# }
# # headers = {
# #     'Content-Type': 'application/json'
# # }
# # response = requests.post(url_anketa,
# #                          headers=headers,
# #                          data=json.dumps(payload))
# response = requests.post(url_anketa, json=payload)
# print(response)
# print(response.status_code)
# pprint(response.json())


# # 1 получить информацию о картинке дня
# url = 'https://api.nasa.gov/planetary/apod'
# params = {
#     'date': '2024-05-12',
#     'api_key': 'xAV7ZrQf0yCNVFKcCa87ujS38lXMiI4mgmpREBBd'
# }
# response = requests.get(url, params=params)
# url_image = response.json()['url']
# file_name = url_image.split('/')[-1]
#
# # 2 скачать картинку дня
# response = requests.get(url_image)
# with open(file_name, 'wb') as f:
#     f.write(response.content)
#
# # 3 создать папку на яндекс диске
# params = {'path': 'Nasa'}
# headers = {'Authorization': 'OAuth y0_AgAAAABnENF7AADLWwAAAADW0Zr0rLgkxmptRpqgS1mkh6kZ5279rAg'}
# response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
#                         params=params,
#                         headers=headers)
#
# # 4 загрузить файл на яндекс диск
# params = {'path': f'Nasa/{file_name}'}
# response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
#                         params=params,
#                         headers=headers)
# url_for_upload = response.json()['href']
#
# with open(file_name, 'rb') as content:
#     requests.put(url_for_upload,
#                  files={'file': content})


# показываю домашку
url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)
# with open('answer.json', 'w') as f:
#     f.write(response.text)

for hero in response.json():
    name = hero['name']
    intelligence = hero['powerstats']['intelligence']
    if intelligence > 90:
        print(f'{name} - {intelligence}')