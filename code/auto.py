# Webscraping (sites) 
from selenium import webdriver
from bs4 import BeautifulSoup 
from selenium.webdriver.common.by import By
import telebot  
import time
import requests 
import boto3
import cv2
import re 

# FAZE DE TESTE
# LEMBRAR DEPOIS DE ARRUMAR A ESTRUTURA DO CÓDIGO, O OBJETIVO POR AGORA È FAZER RODAR

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}
mercado_livre = "https://www.mercadolivre.com.br/ofertas#nav-header"
amazon = "https://www.amazon.com.br/deals?ref_=nav_cs_gb"
BanWords = ['span','tag','style','true']
# Expressão Regular
class auto:
    def RegularExpression(self,x:str):
        NameProdocts = re.findall(r">([^<]+)<",x)
        LinkProdocts = re.findall(r'href="([^"]+)"',x)
        PriceProducts = re.findall(r">([^<]+)<",x)
        NameStore = re.findall(r">([^<]+)<",x)

    def MercadoLivre(self):
        resposta_mercadolivre = requests.get(mercado_livre,headers=headers)
        soup = BeautifulSoup(resposta_mercadolivre.content,'html.parser')
        NameProdoct = str(soup.find_all("h3",class_="poly-component__title-wrapper"))
        NameStore = soup.find_all("span",class_="poly-component__brand")
        Link = str(soup.find("a",class_="poly-component__title"))
        Price = str(soup.find("span",class_="andes-money-amount__fraction"))
        group_id = str(soup.find('div',class_="andes-card poly-card poly-card--grid-card poly-card--large andes-card--flat andes-card--padding-0 andes-card--animated"))
        NameProdocts = re.findall(r">([^<]+)<",NameProdoct)
        LinkProdocts = re.findall(r'href="([^"]+)"',Link)
        self.CliearNameProdocts = [(indice,produto) for indice,produto in enumerate(NameProdocts) if indice % 2 == 0]
        return self.CliearNameProdocts,Link 

    def Amazon(self):
        responsta_amazon = requests.get(amazon,headers=headers)
        soup = BeautifulSoup(responsta_amazon.content,'html.parser')
        NameProdoct = soup.find_all('span',class_="a-truncate-cut")
        Link = None
        Price = soup.find_all("span",class_="a-price-whole") 
        itens_groupy = soup.find_all("div",class_="GridItem-module__container_PW2gdkwTj1GQzdwJjejN")
    
    def save_img(self):
        name_img = ""
        for c in len(1,self.CliearNameProdocts):
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(options=options)
            driver.get("https://www.mercadolivre.com.br/ofertas#nav-header") #Url mecado livre 
            # Pegando os elementos
            id = f":R2{c}j7:"
            xpath = f'//*[@id={id}]'
            name_img = f'img{c}.png'
            ImgElement = driver.find_element(By.XPATH, xpath)
            ImgElement.screenshot(name_img)
            driver.quit()
            BUCKET_NAME = "fileimgbot"
            FILE_PATH = name_img
            S3_OBJECT_NAME = "nome_teste1.png"
            s3 = boto3.client('s3')
            try:
                reponse = s3.list_buckets()
                s3.upload_file(FILE_PATH,BUCKET_NAME,S3_OBJECT_NAME)
                print(f"Arquivo {FILE_PATH} enviado com sucesso para {BUCKET_NAME}/{S3_OBJECT_NAME}")
                print("Buckets existentes: ")
                for bucket in reponse['Buckets']:
                    print(f'{bucket["Name"]}')
            except Exception as e:
                print("Ocorreu um erro {e}")
            path = s3.upload_file(FILE_PATH,BUCKET_NAME,S3_OBJECT_NAME)

s = auto()