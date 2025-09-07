from selenium import webdriver
from bs4 import BeautifulSoup 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests 
import time
import re 



with open("email.txt",'r') as email:
    email = email.read()
login = "https://www.mercadolivre.com/jms/mlb/lgz/msl/login/H4sIAAAAAAAEAzVP2w7CMAj9F57NZpbolj36Iw3b2IbStWnxFuO_SzW-EDg34AUSFt6cPiNBD_SIwiMr7CAK6hySdzwZ4cWgzEr_cSgSTOhJKWXoXyVooelEZipRM0omE-FVVzdLuBv23WUYZ0cP820o7k7Djamwf8cSbFhVY-7rWjgrVp7SiFMQviWqxuCrIdUSzmjFrq_hvTN3VqcJxwv0mq5km2N5BpXD9rv62HT7fdu0rTWHQ9PB-wPpwHdY_wAAAA/user"
mercado_livre = "https://www.mercadolivre.com.br/ofertas#nav-header"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}



resposta_mercadolivre = requests.get(mercado_livre,headers=headers)
soup = BeautifulSoup(resposta_mercadolivre.content,'html.parser')
Link = str(soup.find("a",class_="poly-component__title"))



options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("https://www.mercadolivre.com.br/afiliados/linkbuilder#hub")
campo_email = driver.find_element(By.ID,"user_id")
time.sleep(0.5)
campo_email.send_keys(email)
time.sleep(1)
botao = driver.find_element(By.XPATH, "//input[@type='submit']")
botao = driver.click()
