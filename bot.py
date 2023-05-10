import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from download import youtube2mp3
import os
import json


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
  I am here to help you to convert youtube videos to mp3 without installing any application.\
  """)

@bot.message_handler(commands=['download'])
def start_download(message):
  text = "Please provide the youtube link of the video"
  sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
  bot.register_next_step_handler(sent_msg, day_handler)

def day_handler(message):
  youtube_url = message.text
  bot.send_message(message.chat.id,"Your request is being processed please wait for some time")
  x = youtube2mp3(youtube_url,"assets")
  bot.send_message(message.chat.id,"Your file is ready to be downloaded 🚀")
  bot.send_audio(chat_id=message.chat.id, audio=open(x, 'rb'))
  os.remove(x) #deletes the downloaded file from server.


def checkUserLastMessage(userId):
  """Check for the users last message time"""
  try:
    data = open('data/data.json')
    data = json.load(data)
    filter(lambda user: user['id'] == userId, data)
    
  except:
    print("Something went wrong")
  else:
    print("Nothing went wrong")



bot.infinity_polling()

