from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from nltk.tokenize import RegexpTokenizer
from auto import auto 
from selenium import webdriver 
import nltk 

Auto = auto()
Name,Link = Auto.MercadoLivre()
Name_str = str(Name)
tonizer = RegexpTokenizer(r'\w+')
Tokenizacao = tonizer.tokenize(Name_str)

#frequencia = nltk.FreqDist(Name_str) -> Frequencia dos caracter 

dados_treinamento = [str(dados) for dados in Name]
Divisao = int(len(dados_treinamento) *0.50)
x = str(dados_treinamento[:Divisao])
y = str(dados_treinamento[Divisao:])

x_byte = x.encode('utf-8')
y_byte = y.encode('utf-8')
x_binary = ''.join(format(byte,'08b') for byte in x_byte)
y_binary = ''.join(format(byte,'08b') for byte in x_byte)

'''X_train,X_test,y_train,y_test = train_test_split(x_binary,y_binary,test_size=0.3)
model = RandomForestClassifier(n_estimators=20)
model.fit(X_train,y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test,predictions)
print(accuracy)'''