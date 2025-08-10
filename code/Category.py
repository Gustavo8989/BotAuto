from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from selenium import webdriver
from sklearn.pipeline import Pipeline
from sklearn import svm
from auto import auto
import cv2 
#import spacy 


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("https://www.google.com") #Url mecado livre 

logo = driver.find_element("xpath", '//*[@id="hplogo"]')
logo.screenshot("print_logo.png")
driver.quit()





teste = auto
Name,Link = teste.MercadoLivre()
print(Name)