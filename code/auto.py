# Webscraping (sites) 
from selenium import webdriver
from bs4 import BeautifulSoup 
import pandas as pd 
import numpy as np 
import requests 
import re 


class Webscraping:
    def __init__(self):
        pass 

    def mercadolivre(self):
        url_mercado = 'https://www.mercadolivre.com.br/' 
        response = requests.get(url_mercado) 
        soup = BeautifulSoup(response.text,'html.parser') 
    
    def amazon(self):
        url_amazon = "https://www.amazon.com.br/"
        response = requsts.get(url_amazon) 
        soup = BeautifulSoup(response.text,'html.parser') 

