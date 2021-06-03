import requests
from bs4 import BeautifulSoup

URL = 'https://g1.globo.com/bemestar/coronavirus/noticia/2021/05/23/brasil-tem-449-mil-mortes-por-covid-19.ghtml'
lista = []
numeros = []
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
soup = soup.find(class_='glb-grid')
soup = soup.find(class_='mc-body theme')
soup = soup.find(class_='mc-article-body')
soup = soup.find(itemprop="articleBody")
soup = soup.find(class_='wall protected-content')
soup = soup.find(class_='content-unordered-list')

soup = soup.find_all('li')
for item in soup:
    lista.append(item.text)
    print(item.text + '\n')

n = int(input())

for k in range(n):
    qnt = list(lista[-k].split()[2])
    j = int(qnt[0]+qnt[2]+qnt[3]+qnt[4])
    numeros.append(j)

print("a variação em relação a ontem foi de: ", numeros[-1], numeros[-2])

for i in range(len(lista)):
    print(lista[i] + '\n')