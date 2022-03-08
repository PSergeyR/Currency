import requests
from bs4 import BeautifulSoup
from datetime import datetime
import telebot


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

open_token = open('token.txt', 'r')
str_token = open_token.read()
bot = telebot.TeleBot(str_token)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, course(10))


def token():
    open_token = open('token.txt', 'r')  # Читаем токен из файла
    str_token = open_token.read()
    open_token.close()  # Закрываем файл
    return str_token

# БОТ


bot = telebot.TeleBot(token())


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, course(10))

# Получение сообщений от юзера


@bot.message_handler(content_types=["text"])
def handle_text(message):
        bot.send_message(message.chat.id, 'Сегодня : ' + date_today())


# Запускаем бота
bot.polling(none_stop=True, interval=0)




if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
    print(course(10))  # 10- USA
    print(f'Текущая дата: ' + date_today())

