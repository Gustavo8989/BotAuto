from bs4 import BeautifulSoup
from selenium import webdriver
import requests 
import telebot 
import time 
import re 

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}


# URLs
'''
for c in range(4):
    url_99 = f"https://www.99freelas.com.br/projects?order=numero-de-interessados-menor&page={c}"
    url_workona_0_4 = f"https://www.workana.com/jobs?category=it-programming&language=pt&page={c}"
    page_99 = requests.get(url_99,headers=headers)
    page_workana = requests.get(url_workona_0_4,headers=headers)
    soup_99 = BeautifulSoup(page_99.content, 'html.parser')
    soup_workana = BeautifulSoup(page_workana.content,'html.parser')
    titulo_99 = soup_99.find_all('h1')
    titulo_workana = soup_workana.find_all('h1')
    for titulos in titulo_99:
        title_projects = titulos.find('h1')
        link_project = titulos.find('a')
        print(titulos.text)
    print('-'*30)
    for c in titulo_workana:
        title_projects = c.find('h1')
        link_project = c.find('h1')
        print(c.text)

with open("auth.txt",'r') as arquivo:
    key = arquivo.read()

TOKEN = key 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_menssage(message):
    bot.reply_to(message,"Teste1")

@bot.message_handler(func=lambda msg:True)
def echoa_all(message):
    bot.reply_to(message,message.text)


print("Inicializando um bot")
bot.infinity_polling()''' 

mercado_livre = "https://www.mercadolivre.com.br/ofertas#nav-header"
resposta_mercadolivre = requests.get(mercado_livre,headers=headers)
soup = BeautifulSoup(resposta_mercadolivre.content,'html.parser')
NameProdoct = str(soup.find_all("h3",class_="poly-component__title-wrapper"))
Price = str(soup.find_all("span",class_="andes-money-amount andes-money-amount--cents-superscript"))
Price_ = re.findall(r">([^<]+)<",Price)
NameStore = re.findall(r">([^<]+)<",NameProdoct)

# Limpando os valores 
for indice,produto in enumerate(NameStore):
    if indice % 2 == 0:
        pass 
ClearName = [(indice,produto) for indice,produto in enumerate(NameStore) if indice % 2 == 0]

# Limpando os valores 
limpos = [r.replace(r",","")for r in Price_]
lista_valores_limpa = [c for c in limpos if c.strip()]

driver = webdriver.Chrome()
driver.get("https://www.google.com")
logo = driver.find_element("xpath", '//*[@id="hplogo"]')
logo.screenshot("print_logo.png")
driver.quit()
