import time
import requests
from bs4 import BeautifulSoup

BASE_URL= "https://arxiv.org/html/24"
MONTH_LIST = [i for i in range(1,5)]
ARTICLE_LIST= [i for i in range(1,16)]


urls= []


#cerco di accedere alla parte successiva del sito, strutturata in questo modo:  
# sito_base/anno/n_documento/section/num_sezione
def UrlGenerators():
    for m in MONTH_LIST:
        for a in ARTICLE_LIST:
            url=BASE_URL+str(m).zfill(2)+"."+str(a).zfill(5)+"v1"
            if CheckConn(url):
                urls.append(url)
    writer(urls)
    return urls



def CheckConn(url):
    time.sleep(1)
    response = requests.get(url)
        #controllo che la connessione avvenga correttamente
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titolo = soup.find('h1').text.strip()
        return "No HTML" not in titolo
    else:
        return False


def writer(urls):
    file=open("WebScraping/src/dates.txt", "w")
    for url in urls : file.write(url); file.write("\n") 

