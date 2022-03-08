import requests
from bs4 import BeautifulSoup
from datetime import datetime


def date_today():

    date = str(datetime.now()).split(' ')  # Откидываем лишнюю информацию из выдачи
    date_now = date[0].replace('-', '/').split('/')  # Заменяем - на /
    today = str(date_now[2]+ "/" + date_now[1] + "/" + date_now[0])  # Разворачиваем дату как нужно для запроса
    return today


def course(valute):

    cbr_adress = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_today()}'
    xml_page = requests.get(cbr_adress)
    soup = BeautifulSoup(xml_page.content, 'lxml')
    # print(soup)
    result = str(soup)
    lst = result.split('</valute>')  # Делаем список из xml таким образом из-за специфики форматирования файла
    split_lst = str(lst[valute])  # Выбираем нужную валюту для выдачи
    # print(split_lst)
    res2 = split_lst.replace('>', ' ').split('<')  # Отрезаем все лишнее
    return (res2[8] + ',' + res2[10]).replace('name', '').replace('value', ':')  # Делаем ноормальную выдачу


if __name__ == '__main__':
    print(course(10))  # 10- USA
    print(f'Текущая дата: ' + date_today())












