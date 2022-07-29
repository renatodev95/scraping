import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

def launch_browser():
    options = Options()
    options.add_argument('window-size=400,800')
    browser = webdriver.Chrome(options=options)
    browser.get('https://www.airbnb.com')
    return browser;


navegador = launch_browser()
sleep(5)
button = navegador.find_element(By.TAG_NAME, 'button')
button.click()
sleep(5)
input_place = navegador.find_element(By.TAG_NAME, 'input')
input_place.send_keys('São Paulo')
input_place.submit()
# site = BeautifulSoup(navegador.page_source, 'html.parser')
# print(site.prettify())
