import requests


UK_CITIES = [
    'Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh',
    'Norwich', 'York'
]


def find_uk_city(coordinates):
    res = []
    for latitude, longitude in coordinates:
        url = f'https://geocode.maps.co/reverse?lat={latitude}&lon={longitude}&api_key=66a277df2dea2357414732jwd244077'
        response = requests.get(url)
        if 200 <= response.status_code < 300:
            data = response.json()
            city = data['address']['city']
            if city in UK_CITIES:
                res.append(city)
        else:
            print(
                f"Error: API request failed with status code {response.status_code}"
            )
    return (' '.join(res))


print(find_uk_city([
    ('55.7514952', '37.618153095505875'),
    ('52.3727598', '4.8936041'),
    ('53.4071991', '-2.99168')
]))
