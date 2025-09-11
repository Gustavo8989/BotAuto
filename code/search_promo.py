from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import requests 
import telebot 


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}

# Lista dos componentes que o Bot vai pesquisar
list_components = {"Placa de mãe":"Asus TUF GAMING B550M-Plus",
                   "Processador":"AMD Ryzen 5 4500",
                   "Plava de video":"XFX Radeon RX 6600",
                   "Ram":"Kingston Fury Beast 16GB (2x8GB) DDR4 3200MHz",
                   "SSD":"Kingston NV3 1TB M.2 NVMe Gen4",
                   "Fonte":"Corsair CX550 550W 80 Plus Bronze",
}

value_search = []

for c in list_components:
    value_search.append(list_components[c]) 


# gerando URL 




# Pesquisando no google:
option = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=option)
driver.get("https://www.google.com/?zx=1757252597559&no_sw_cr=1")
search = driver.find_element(By.ID,"APjFqb")
search.send_keys()

