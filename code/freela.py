from bs4 import BeautifulSoup
from time import sleep
import selenium 
import requests
import re

# URLs 
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}
cronometro = 10
class freelas:
    def __init__(self):
        pass 
    def freelas_99(self,url):
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.content,'html.parser')
        titulo = soup.find_all('h1')
        for titulos in titulo:
            project_title = titulos.find('h1')
            link_project = titulos.find('a')
            project_title = titulos.text
            print(project_title)
            print(link_project)
            print('-'*30)

    def workana(self,url):
        sleep(5) # Quando for para produção colocar 1 minuto 
        response_workana = requests.get(url,headers=headers)
        soup_workana = BeautifulSoup(response_workana.content,'html.parser')
        project = soup_workana.find_all('h1')
        for projects in project:
            projects_title_w = projects.find('h1')
            link = projects.find('a')
            projects_title_w = projects.text
            print(projects_title_w)
            print(link)
            print('-'*30)


for c in range(4):
    url_99 = f"https://www.99freelas.com.br/projects?order=numero-de-interessados-menor&page={c}"
    url_workona_0_4 = f"https://www.workana.com/jobs?category=it-programming&language=pt&page={c}"
    teste = freelas() 
    teste.freelas_99(url_99)
    teste.workana(url_workona_0_4)