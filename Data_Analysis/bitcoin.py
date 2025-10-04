# Analise do preço do bitcoin para com series temporais 

import requests 


price_usd = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCBRL").json()
price_usd = float(price_usd["price"])
price_usd = round(price_usd,2)

