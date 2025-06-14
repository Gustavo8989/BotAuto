from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import re


url_99 = "https://www.99freelas.com.br/projects?order=numero-de-interessados-menor&categoria=web-mobile-e-software"
url_workona_0_4 = "https://www.workana.com/jobs?category=it-programming&has_few_bids=1&language=pt"
url_workana_4_x = "https://www.workana.com/pt/jobs?category=it-programming&has_few_bids=2&language=pt"
class freelas:
    def regular_expression(self):
        print('')
    
    def freelas_99(self,url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text,'html.parser')
        print(soup)


teste = freelas() 
teste.freelas_99(url_99)
