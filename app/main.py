import os

import telebot
from telebot import types

from app.handlers import haha

TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_keyboard(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)

    itembtn1 = types.KeyboardButton('Добавить дело в список')
    itembtn2 = types.KeyboardButton('Показать список дел')
    itembtn3 = types.KeyboardButton('Удалить дело из списка')
    itembtn4 = types.KeyboardButton("Удалить все дела из списка")
    itembtn5 = types.KeyboardButton('Другое')
    itembtn6 = types.KeyboardButton('Пока все!')

    keyboard.add(itembtn1, itembtn2)
    keyboard.add(itembtn3, itembtn4, itembtn5, itembtn6)

    msg = bot.send_message(
        chat_id=message.from_user.id,
        text="Нажми на кнопку!", 
        reply_markup=keyboard,
    )

    bot.register_next_step_handler(msg, add_case)

def add_case(message):
    bot.send_message(
        chat_id=message.from_user.id,
        text="Дело добавлено!", 
    )

@bot.message_handler(regexp='^\d{8}$')
def bd(message):
    bot.send_message(
        chat_id=message.from_user.id,
        text=f"Твой др {message.text}!",
    )

@bot.message_handler(content_types='text')
def echo(message):

    bot.send_message(
        chat_id=message.from_user.id,
        text=message.text,
    )

bot.polling(none_stop=True)
