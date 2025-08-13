from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from selenium import webdriver
from sklearn.pipeline import Pipeline
from sklearn import svm
from auto import auto
import pytesseract
import cv2 
import nltk 

#Colocar as IMG em um banco de dados AWS 

Category = ["Técnologia","Veiculos","Eletrodomesticos","Roupa","Livros"] # Acresentar mais 
teste = auto
Name,Link = teste.MercadoLivre()

# O Processamento de linguagem natural vai ser realizado de duas formas (Pegando informações atraves da img e do texto)
#IMG
imagem_path = "teste.png"
imagem = cv2.imread(imagem_path)
if imagem is None:
    print("Erro ao carregar a IMG")
# Fazendo um pré-pricessamento para facilitar na leitura dos dados 
imagem_cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
imagem_binario = cv2.threshold(imagem_cinza,128,255,cv2.THRESH_BINARY)
'''cv2.imshow("Teste",imagem_cinza)
cv2.waitKey(0)
'''
nltk.download()