from telebot import TeleBot
from config import TELEGRAM_TOKEN

TOKEN = TELEGRAM_TOKEN

if TOKEN is None : 
    raise ValueError("No se ha encontrado el token de Telegram")

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello, I'm bot!")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True, interval=0)