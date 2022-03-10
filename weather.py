import requests
from bs4 import BeautifulSoup

URL = 'https://www.gismeteo.ru/weather-perm-4476/tomorrow/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
           'accept': '*/*'}

def weather_tomorrow(params=None):
    html = requests.get(URL, headers=HEADERS, params=params)
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('div', class_='weathertabs')

    for item in items:
        tomorrow = str(item.find('a', class_='weathertab-block').get_text(' '))
    result = tomorrow.split(' ')
    result1 = (result[0]).strip(',') + ": \n днем: " + result[6] + '; ночью:' + result[4] + ' градусов'
    print(result1)
    return result1



