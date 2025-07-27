from bs4 import BeautifulSoup
from time import sleep
import telebot
import requests
import re

# URLs 
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}
cronometro = 10
class freelas:
    with open("auth.txt",'r') as arquivo:
        key = arquivo.read()
    TOKEN = key
    global bot 
    bot = telebot.TeleBot(TOKEN)

    def freelas_99(self,url):
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.content,'html.parser')
        titulo = soup.find_all('h1')
        for titulos in titulo:
            project_title = titulos.find('h1')
            self.link_project = titulos.find('a')
            self.project_title = titulos.text
    def workana(self,url):
        sleep(5) # Quando for para produção colocar 1 minuto 
        response_workana = requests.get(url,headers=headers)
        soup_workana = BeautifulSoup(response_workana.content,'html.parser')
        project = soup_workana.find_all('h1')
        for projects in project:
            projects_title_w = projects.find('h1')
            self.link = projects.find('a')
            self.projects_title_w = projects.text
            
    @bot.massage_handler(commands=['start'])
    def send_projects(message):
        bot.reply_to(message,'Teste')
    @bot.message_handler(func=lambda msg:True)
    def echoa_menssage(message):
        bot.reply_to(message,message.text)



for c in range(4):
    url_99 = f"https://www.99freelas.com.br/projects?order=numero-de-interessados-menor&page={c}"
    url_workona_0_4 = f"https://www.workana.com/jobs?category=it-programming&language=pt&page={c}"
    teste = freelas() 
    teste.freelas_99(url_99)
    teste.workana(url_workona_0_4)