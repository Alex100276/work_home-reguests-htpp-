import requests

UK_CITIES = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']


def find_uk_city(coordinates: object) -> object:
    for lat, lon in coordinates:
        response = requests.get(f'https://geocode.maps.co/reverse?lat={lat}&lon={lon}')
        data = response.json()
        city = data['address']['city']
        if city in UK_CITIES:
            return city

        
print(find_uk_city([
    ('55.7514952', '37.618153095505875'),
    ('52.3727598', '4.8936041'),
    ('53.4071991', '-2.99168')
]))
