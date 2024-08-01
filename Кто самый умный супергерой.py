import requests


def get_the_smartest_superhero() -> str:
    the_smartest_superhero = ''
    hero_name = ["Hulk", "Captain America", "Thanos"]
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        superhero_list = response.json()
        intelligence_list = []
        for superhero in superhero_list:
            if superhero['name'] in hero_name:
                intelligence_list.append(superhero['name'])
                intelligence_list.append(superhero['powerstats']['intelligence'])
                the_smartest_superhero = superhero['name']

    return the_smartest_superhero


print(get_the_smartest_superhero())
