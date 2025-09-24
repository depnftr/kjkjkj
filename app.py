import telebot
from telebot import types

API_TOKEN = "8473346638:AAEpDDvaxh3XFMd6RoeQtXBbSOasrZ3Pvks" 
WEBAPP_URL = "http://127.0.0.1:5000" 

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    play_btn = types.InlineKeyboardButton(
        "🚀 Играть в Авиатор", web_app=types.WebAppInfo(WEBAPP_URL)
    )
    markup.add(play_btn)
    bot.send_message(message.chat.id, "Привет! Я бот Авиатор 🚀", reply_markup=markup)

print("Бот запущен!")
bot.polling(none_stop=True)