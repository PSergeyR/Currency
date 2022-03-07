import requests
from bs4 import BeautifulSoup
import lxml
from datetime import datetime, date


date = str(datetime.now()).split(' ')
date_now = date[0].replace('-', '/').split('/')


cbr_adress = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_now[2]+ "/" + date_now[1] + "/" + date_now[0]}'
xml_page = requests.get(cbr_adress)
soup = BeautifulSoup(xml_page.content, 'lxml')
#print(soup)


result = str(soup)
lst = result.split('</valute>')
split_lst = str(lst[10])
#print(split_lst)
res2 = split_lst.replace('>', ' ').split('<')
print((res2[8] + ','+ res2[10]).replace('name', '').replace('value', ':'))
#














