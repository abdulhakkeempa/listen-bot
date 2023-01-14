#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os


#loading env variables
load_dotenv()

#telegram api configuration
API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
  username = message.from_user.first_name
  bot.reply_to(message, f"""\
  Hi {username}, I am Chill Here Bot.
  I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
  """)


@bot.message_handler(commands=['download'])
def start_download(id):
  bot.reply_to(id,"Please provide the youtube link")


bot.infinity_polling()


# def gen_markup():
#     markup = InlineKeyboardMarkup()
#     markup.row_width = 2
#     markup.add(InlineKeyboardButton("Youtube to MP3", callback_data="download"),
#                                InlineKeyboardButton("Quit", callback_data="cb_no"))
#     return markup

# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     if call.data == "download":
#         # start_download(call.id)
#         print(call.id)
#         bot.answer_callback_query(call.id, text='Command executed')
#     elif call.data == "cb_no":
#         bot.answer_callback_query(call.id, "Answer is No")

# @bot.message_handler(commands=['help'])
# def message_handler(message):
#     print(message.chat.id)
#     bot.send_message(message.chat.id,"Please choose the option", reply_markup=gen_markup())

