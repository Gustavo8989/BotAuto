from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn import svm
from nltk.tokenize import RegexpTokenizer
from auto import auto
import nltk 

teste = auto
Name,Link = teste.MercadoLivre()
Name_str = str(Name)
tonizer = RegexpTokenizer(r'\w+')
Tokenizacao = tonizer.tokenize(Name_str)

#frequencia = nltk.FreqDist(Name_str) -> Frequencia dos caracter 

dados_treinamento = [str(dados) for dados in Name]
vectorize = TfidfVectorizer()
x = vectorize.fit_transform(dados_treinamento)
kMeans = KMeans(n_clusters=17,random_state=42)
kMeans.fit(x)
