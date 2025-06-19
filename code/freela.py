from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import urllib 
import requests
import re


url_99 = "https://www.99freelas.com.br/projects?order=numero-de-interessados-menor&categoria=web-mobile-e-software"
url_workona_0_4 = "https://www.workana.com/jobs?category=it-programming&has_few_bids=1&language=pt"
url_workana_4_x = "https://www.workana.com/pt/jobs?category=it-programming&has_few_bids=2&language=pt"
class freelas:
    def regular_expression(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}
        print('')
    
    def freelas_99(self,url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text,'html.parser')
        projetos = soup.find_all('li', class_='with-flag result-item first-with-flag')
        print(projetos)


teste = freelas() 
teste.freelas_99(url_99)
