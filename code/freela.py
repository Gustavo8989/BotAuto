from bs4 import BeautifulSoup
from time import sleep
import telebot
import requests
import re

# FAZE DE TESTE
# LEMBRAR DEPOIS DE ARRUMAR A ESTRUTURA DO CÓDIGO, O OBJETIVO E FAZER RODAR

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}
cronometro = 10
def freela():
    # Laço de repetição para acessar as paginas do site 
    urls_99 = [f"https://www.99freelas.com.br/projects?order=numero-de-interessados-menor&page={c}" for c in range(4)]
    urls_workona_0_4 = [f"https://www.workana.com/jobs?category=it-programming&language=pt&page={c}" for c in range(4)] 
    title_projects_99 = []
    title_projects_workana = []
    link_project_99 = []
    link_project_workana = []

    # Abrindo a chave e inicializando o bot
    with open("auth.txt",'r') as arquivo:
        key = arquivo.read()
    TOKEN = key
    global bot 
    bot = telebot.TeleBot(TOKEN)

    # Webscraaping na 99 freelas
    for url in urls_99:
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.content,'html.parser')
        titulo = soup.find_all('h1')
        for titulos in titulo:
            project_title = titulos.find('h1')
            link_project = titulos.find('a')
            project_title = titulos.text
            title_projects_99.append(project_title)
            link_project_99.append(link_project)

    # Webscraaping na Workana
    for url in urls_workona_0_4:
        response_workana = requests.get(url,headers=headers)
        soup_workana = BeautifulSoup(response_workana.content,'html.parser')
        project = soup_workana.find_all('h1')
        for projects in project:
            projects_title_w = projects.find('h1')
            link_w = projects.find('a')
            projects_title_w = projects.text
            title_projects_workana.append(projects_title_w)
            link_project_workana.append(link_w)
    
    @bot.message_handler(commands=['start'])
    def send_projects(message):
        bot.reply_to(message,'Você quer ver da 99 Freelas ou da Workana')

    @bot.message_handler(commands=['99 Freelas'])
    def echoa_menssage(message):
        for projects in title_projects_99:
            bot.reply_to(message,projects)

    
    bot.infinity_polling()

teste = freela()
teste 