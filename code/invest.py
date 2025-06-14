import requests 
import pandas as pd 
import telebot
import finnhub 
import time 
import os 

def invest(api,money_invest,key_finnhub):
    dolar = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    dolar_response = requests.get(dolar) 
    dolar_real = float(dolar_response.json()['USDBRL']['bid'])
    alphavantage = requests.get(api) 
    data_alphavantage = alphavantage.json()
    data_finnhub = finnhub.Client(api_key=key_finnhub)
    print(data_alphavantage) 



invest('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo',500,open("key_api_finnhub.txt","r"))
