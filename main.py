import requests
from bs4 import BeautifulSoup
from datetime import datetime
import telebot
from telebot import types



def date_today():

    date = str(datetime.now()).split(' ')  # Откидываем лишнюю информацию из выдачи
    date_now = date[0].replace('-', '/').split('/')  # Заменяем - на /
    today = str(date_now[2] + "/" + date_now[1] + "/" + date_now[0])  # Разворачиваем дату как нужно для запроса
    return today


def course(valute):

    cbr_adress = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_today()}'
    xml_page = requests.get(cbr_adress)
    soup = BeautifulSoup(xml_page.content, 'lxml')
    # print(soup)
    result = str(soup)
    lst = result.split('</valute>')  # Делаем список из xml таким образом из-за специфики форматирования файла
    split_lst = str(lst[valute])  # Выбираем нужную валюту для выдачи
    #print(lst)
    res2 = split_lst.replace('>', ' ').split('<')


    # Отрезаем все лишнее

    return (res2[8] + ' ' + res2[10]).replace('name', '').replace('value', ':') # Делаем ноормальную выдачу


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
    # Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("дата")
    item2 = types.KeyboardButton("курс")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Бот стартовал!', reply_markup=markup)




@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем дату
    if message.text.strip() == 'дата':
        bot.send_message(message.chat.id, 'Сегодня : ' + date_today())
        print(date_today())
    # Если юзер прислал 2, выдаем курс
    elif message.text.strip() == 'курс':
        bot.send_message(message.chat.id, 'Курс валют на сегодняшнее число: ' + course(10) + ',' '\n' + course(11))
        print(course(10))





@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'дата':
        bot.send_message(message.chat.id, 'Сегодня : ' + date_today())
    if message.text == 'курс':
        bot.send_message(message.chat.id, 'Курс доллара на сегодняшнее число:' + course(10))


# Запускаем бота
bot.polling(none_stop=True, interval=0)




if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
    print(course(10))  # 10- USA
    print(f'Текущая дата: ' + date_today())

