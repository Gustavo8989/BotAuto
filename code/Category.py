from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from selenium import webdriver
from sklearn.pipeline import Pipeline
from sklearn import svm
from auto import auto
import cv2 
#import spacy 
Category = ["Técnologia","Veiculos","Eletrodomesticos","Roupa","Livros"] # Acresentar mais 




teste = auto
Name,Link = teste.MercadoLivre()
print(Link)