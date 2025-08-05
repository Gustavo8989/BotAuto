# Webscraping (sites) 
from selenium import webdriver
from bs4 import BeautifulSoup 
import telebot  
import requests 
import re 

# FAZE DE TESTE
# LEMBRAR DEPOIS DE ARRUMAR A ESTRUTURA DO CÓDIGO, O OBJETIVO POR AGORA È FAZER RODAR

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}
oferta_merca = "https://www.mercadolivre.com.br/ofertas#nav-header"
amazon = "https://www.amazon.com.br/deals?ref_=nav_cs_gb"
# Expressão Regular
def RegularExpression(x:str):
    NameProdocts = re.findall(r"[a-zA-Z]",x)

def MercadoLivre():
    resposta_mercadolivre = requests.get(oferta_merca,headers=headers)
    soup = BeautifulSoup(resposta_mercadolivre.content,'html.parser')
    NameProdoct = str(soup.find_all("h3",class_="poly-component__title-wrapper"))
    NameStore = soup.find_all("span",class_="poly-component__brand")
    Link = soup.find_all("a",class_="poly-component__title")
    Price = soup.find_all("div",class_="poly-price__current")
    itens_grupy = soup.find_all("div",class_="items-with-smart-groups")
def Amazon():
    responsta_amazon = requests.get(amazon,headers=headers)
    soup = BeautifulSoup(responsta_amazon.content,'html.parser')
    NameProdoct = soup.find_all('span',class_="a-truncate-cut")
    Link = None
    Price = soup.find_all("span",class_="a-price-whole") 
    itens_groupy = soup.find_all("div",class_="GridItem-module__container_PW2gdkwTj1GQzdwJjejN")
    print(NameProdoct)

MercadoLivre()

'''
TIRANDO PRINT EM SELENIUM

driver = webdriver.Chrome()
driver.get("https://www.google.com")
logo = driver.find_element("xpath", '//*[@id="hplogo"]')
logo.screenshot("print_logo.png")
driver.quit()


'''