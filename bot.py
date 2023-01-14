import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from download import youtube2mp3
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
  os.remove(x)

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

