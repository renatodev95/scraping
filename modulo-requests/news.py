import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/df/distrito-federal/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# Obtendo HTML da noticia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    resumo = noticia.find('div', attrs={'class': re.compile('feed-post-body-resumo')})
    if resumo:
        lista_noticias.append([titulo.text, resumo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '',titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])

news.to_excel('noticias.xlsx', index=False)