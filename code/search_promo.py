from requests.api import options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests 
import telebot 

# A Build dois esta com as melhores peças custo beneficios

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}

# Lista dos componentes que o Bot vai pesquisar
pc_one = [
    "Asus TUF GAMING B550M-PLUS",
    "AMD Ryzen 5 4500",
    "XFX Radeon RX 6600",
    "Kingston Fury Beast 16GB (2x8GB) DDR4 3200MHz",
    "Kingston NV3 500GB M.2 NVMe Gen4",
    "Corsair CX550 550W 80 Plus Bronze",
    "Gabinete gamer com pelo menos 1 ventoinha inclusa"
]



# MELHOR
pc_two =[
    "AMD Ryzen 5 5500 (6 núcleos, 12 threads, 3.6 GHz base)",
    "ASRock B450M Steel Legend",
    "ASRock Radeon RX 7600 Steel Legend 8GB GDDR6",
    "16GB (2x8GB) DDR4 3200MHz Kingston Fury Beast",
    "SSD Kingston NV3 1TB M.2 NVMe Gen3",
    "Fonte Corsair CV550 550W 80 Plus Bronze",
    "Gabinete Gamer com pelo menos uma ventoinha inclusa"
]


component = []

for index,nome in enumerate(pc_two):
    option = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=option)
    driver.get("")
    search = driver.find_element(By.ID,"APjFqb")
    search.send_keys(nome + " Promoção" + Keys.ENTER)

