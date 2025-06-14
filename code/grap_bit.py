import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import requests 
import telebot 
import time
import os

class telegram_bitcoin:
    def price(self,api,price_applied:float,frame):
        # Bitcoin 
        price_bitcoin = requests.get(api)
        data = price_bitcoin.json() 
        price =float(data['price'])
        # Real and Dolar 
        dolar_em_real = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        brl_response = requests.get(dolar_em_real) 
        usd_to_brl = float(brl_response.json()['USDBRL']['bid'])
        # Conversão 
        self.bitcoin_to_real =  price * usd_to_brl 
        my_money = price_applied 
        qtd_brl_bit = float(my_money / self.bitcoin_to_real)
        my_money_all = qtd_brl_bit * self.bitcoin_to_real

        # Create graphic 


    token = os.environ.get('auth.env')
    bot = telebot.TeleBot(token) 
    @bot.message_handler(commands=['price']) 
    def send_welcome(self,message):
        bot.reply_to(message,f"{self.bitcoin_to_real}")

    @bot.message_handler(func=lambda msg:True)
    def message_all(self,message):
        bot.reply_to(message,"Comando negado, para ver o preço digite PRICE")

bot.infinity_polling()
if __name__ == "__main__":
    price = telegram_bitcoin()
    while True:
        price("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",200,100)
        print('-'*40) 
        time.sleep(10) 

# 
