import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import re


def launch_browser():
    options = Options()
    options.add_argument('window-size=400,800')
    browser = webdriver.Chrome(options=options)
    browser.get('https://www.kabum.com.br/minha-conta/favoritos')
    return browser;


navegador = launch_browser()
navegador.maximize_window()

sleep(3)
inputLogin = navegador.find_element(By.ID, 'inputUsuarioLogin')
inputLogin.send_keys('---login---')

sleep(1)
inputSenha = navegador.find_element(By.ID, 'inputSenhaLogin')
inputSenha.send_keys('---senha---')

sleep(1)
botaoLogin = navegador.find_element(By.ID, 'botaoLogin')
botaoLogin.click()

sleep(3)
botaoCloseAd = navegador.find_element(By.CLASS_NAME, 'IconClose')
botaoCloseAd.click()

sleep(3)
botaoFavoritos = navegador.find_element(By.ID, 'linkFavoritosHeader')
botaoFavoritos.click()

sleep(2)
pageContent = navegador.page_source
site = BeautifulSoup(pageContent, 'html.parser')
produtos = site.findAll('div', attrs={'class': re.compile('cardFavoriteContainer')})

lista_produtos = []
for produto in produtos:
    spans = produto.findAll('span')
    link = produto.find('a')
    lista_produtos.append([spans[0].text, float(spans[1].text.replace('R$ ', '')), 'https://www.kabum.com.br' + link['href']])

data_frame = pd.DataFrame(lista_produtos, columns=['Nome', 'Preço', 'Link'])
data_frame.to_csv('kabum.csv', index=False)
