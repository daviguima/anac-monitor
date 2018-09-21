from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup
def read_url(url):
    url = url.replace(" ","%20")
    req = Request(url)
    a = urlopen(req).read()
    soup = BeautifulSoup(a, 'html.parser')
    x = (soup.find_all('a'))
    for i in x:
        file_name = i.extract().get_text()
        url_new = url + file_name
        url_new = url_new.replace(" ","%20")
        if(file_name[-1]=='/' and file_name[0]!='.'):
            read_url(url_new)
        print(url_new)




url = 'http://www.anac.gov.br/assuntos/setor-regulado/aerodromos/cadastro-de-aerodromos/aerodromos-cadastrados/'

read_url(url)