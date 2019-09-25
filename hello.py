import requests
from bs4 import BeautifulSoup
from datetime import datetime

f = open("score.txt", "a+")
timestamp = datetime.now()
f.write('-------' + timestamp.strftime("%Y/%m/%d, %H:%M:%S") + '-------' + '\n')
def web(page, WebUrl):
    if(page > 0):
        url = WebUrl
        code = requests.get(url)
        plain = code.content
        s = BeautifulSoup(plain, "html.parser")
        for value in s.find_all(class_='archive__item-title'):
            #print(value.get_text())
            value = value.get_text().strip()
            f.write(value + '\n')

web(1,'https://objectprogr.github.io/')
f.close()