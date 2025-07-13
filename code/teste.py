from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import selenium
import urllib
import requests
import re

# URLs
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}

for c in range(6):
    url_99 = f"https://www.99freelas.com.br/projects?order=numero-de-interessados-menor&categoria=web-mobile-e-software={c}"
    url_workona_0_4 = f"https://www.workana.com/jobs?category=it-programming&language=pt&page={c}"
    page = requests.get(url_99,headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    titulo = soup.find_all('h1')
    for titulos in titulo:
        title_projects = titulos.find('h1')
        link_project = titulos.find('a')
        print(titulos.text)
        print(link_project)
