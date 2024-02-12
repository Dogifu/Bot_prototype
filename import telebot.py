import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot('6975542663:AAEmEWz2GbZaLJHmgfGs44SjEk9csMG_VSg')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.reply_to(message, 'Привет!')


# bot.polling(none_stop = True)
bot.infinity_polling()
