import requests


def get_the_smartest_superhero(superheros: list) -> str:
    base_url = "https://akabab.github.io/superhero-api/api"
    max_intelligence = 0
    the_smartest_superhero = ''
    for superhero_id in superheros:
        url = f"{base_url}/id/{superhero_id}.json"
        response = requests.get(url)
        info = response.json()
        intelligence = info['powerstats']['intelligence']
        if intelligence > max_intelligence:
            max_intelligence = intelligence
            the_smartest_superhero = info['name']
    return the_smartest_superhero


print(get_the_smartest_superhero([332, 149, 655]))

