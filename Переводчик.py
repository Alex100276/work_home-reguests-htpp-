import requests

url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
token = 'dict.1.1.20240801T035103Z.84cb457d76433ebd.fc4b94d337fd525dd6c515e25249c7b728ca7fa5'  # Замените на свой токен


def translate_word(word):  # Функция для перевода слова
    payload = {'key': token, 'text': word, 'lang': 'ru-en'}  # Параметры запроса
    response = requests.get(url, params=payload)  # Отправляем запрос
    if 200 <= response.status_code < 300:  # Если запрос прошел успешно
        result = response.json()  # Получаем ответ в формате JSON
        if result['def']:  # Если слово найдено
            trans_word = result['def'][0]['tr'][0]['text']  #
            return trans_word
        else:
            return 'Перевод не найден'
    else:
        return 'Ошибка при загрузке перевода'


if __name__ == '__main__':
    word = 'машина'
    trans_word = translate_word(word)
    print(trans_word)
