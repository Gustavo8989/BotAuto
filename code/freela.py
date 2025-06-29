from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import selenium 
import urllib 
import requests
import re

# URLs 
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}

class freelas:
    def __init__(self):
        pass 

    def freelas_99(self,url):
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.content,'html.parser')
        titulo = soup.find_all('h1')
        for titulos in titulo:
            titulo_projetos = titulos.find('h1')
            link_project = titulos.find('a') 
            #clear_link = re.
            project_title = titulos.text 
            print(project_title) 


    def workana(self,url):
        response_workana = requests.get(url,headers=headers)
        soup_workana = BeautifulSoup(response_workana.content,'html.parser')
        project = soup_workana.find_all('span')
        for projects in project:
            projects_ = projects.find('span')
           # print(projects.text) 

for c in range(6):
    url_99 = f"https://www.99freelas.com.br/projects?order=numero-de-interessados-menor&categoria=web-mobile-e-software={c}"
    print(url_99)
    url_workona_0_4 = f"https://www.workana.com/jobs?category=it-programming&language=pt&page={c}"
    teste = freelas() 
    teste.freelas_99(url_99)
    teste.workana(url_workona_0_4)

'''page = requests.get(url_99,headers=headers) 
soup = BeautifulSoup(page.content, 'html.parser') 
titulo = soup.find_all('h1')
for titulos in titulo:
    title_projects = titulos.find('h1')
    link_project = titulos.find('a') 
    print(titulos.text)
    print(link_project)'''  



