from auto import auto
import telebot 


IMG = auto.save_img()



with open("auth.txt") as key:
    key = key.read()

TOKEN = key
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.reply_to(message,"")

bot.infinity_polling()
