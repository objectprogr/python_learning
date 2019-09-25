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
            # [EN] strip() remove new lines from results
            # ---
            # [PL] strip() usuwa nam wszystkie nowe linie w wynikach
            value = value.get_text().strip()
            # [EN] we adding new line after remove new lines above, because
            # in this case we dont`t have empty lines between results
            # ---
            # [PL] dodajemy w tym miejscu nowa linie po kazdym znalezionym elemencie
            # poniewaz, wynik jest w ladniejszej formie, tzn. nie mamy pustych linii
            # pomiedzy wynikami. Gdybysmy wyzej nie usuneli wszystki nowych linii i nie dodali
            # w tym miejscu nowych, to mielibysmy cos takiego: wynik pusta linia wynik pusta linia
            f.write(value + '\n')

web(1,'https://objectprogr.github.io/')
f.close()