# Webscraping (sites) 
from selenium import webdriver
from bs4 import BeautifulSoup 
import telebot  
import requests 
import re 

# FAZE DE TESTE
# LEMBRAR DEPOIS DE ARRUMAR A ESTRUTURA DO CÓDIGO, O OBJETIVO POR AGORA È FAZER RODAR

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}


oferta_merca = "https://www.mercadolivre.com.br/ofertas#nav-header"
amazon = "https://www.amazon.com.br/deals?ref_=nav_cs_gb"

def MercadoLivre():
    resposta_mercadolivre = requests.get(oferta_merca,headers=headers)
    soup = BeautifulSoup(resposta_mercadolivre.content,'html.parser')
    NameProdoct = None 
    Link = None 
    Price = None 
    PriceOriginal = None 
    Category = None 
    Assessment = None 

def Amazon():
    responsta_amazon = requests.get(amazon,headers=headers)
    soup = BeautifulSoup(responsta_amazon.content,'html.parser')
    NameProdoct = None 
    Link = None 
    Price = None 
    PriceOriginal = None 
    Category = None 
    Assessment = None 

