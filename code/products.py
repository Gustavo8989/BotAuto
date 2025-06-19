from selenium import webdriver 
from bs4 import BeautifulSoup
import pandas as pd 
import requests 
import re 


class code:
    def __init__(self,site):
        self.site = site 

    def Webscraping(self):
        response = requests.get(self.site)
        soup = BeautifulSoup(response.text,'html.parser') 


teste = code()
