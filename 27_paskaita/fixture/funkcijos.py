import requests
def apskaiciuoti_plota(ilgis, plotis):
    return ilgis * plotis

def gauti_orus(miestas):
    response = requests.get(f'https://api.weather.com/{miestas}')
    data = response.json()
    return data ['temperatura']

def apsirengti_siltai(miestas):
    temperatura = gauti_orus(miestas)
    if temperatura > 20:
        return False
    return True
