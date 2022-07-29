from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def launch_browser():
    browser = webdriver.Edge()
    browser.get('https://www.walissonsilva.com/blog')
    return browser;


navegador = launch_browser()
sleep(2)
navegador.maximize_window()
elemento = navegador.find_element(By.TAG_NAME, 'input')
elemento.send_keys('data')
sleep(2)
navegador.quit()
