import Constants as keys
import telebot
from telebot import types

bot = telebot.TeleBot(keys.API_KEY,parse_mode=None)

@bot.message_handler(commands=["help","hello"])
def send_help_message(msg):
    print(msg)
    bot.reply_to(msg,"hello this is a test bot")

@bot.message_handler(commands=["aya"])
def send_help_message(msg):
    bot.reply_to(msg,"بسم الله الرحمان الرحيم")
@bot.message_handler(commands=["numberofBismillah"])
def send_help_message(msg):
    bot.reply_to(msg,"there are 114 bismillah in Quran")

@bot.message_handler(content_types=["photo", "sticker"])
def send_content_message(msg):
    print(msg)
    bot.reply_to(msg, "that's not a text message")

#@bot.message_handler(func=lambda msg: msg.from_user.last_name == "Lary")
@bot.message_handler(commands=["sohal"])
def send_multi_message(msg):
    bot.send_poll(
        chat_id=msg.chat.id,
        question="the first pillar in islam",
        options=["shahada","salat","zakat"]
    )

@bot.message_handler(func=lambda msg:msg.text == "surahfatiha")
def send_multi_message(msg):
    bot.send_message(
        chat_id=msg.chat.id,
        text="سورة الفاتحة بصوت الشيخ ماهر المعيقلي استمع"
    )
    with open(r"C:\Users\aminelary\Desktop\fatiha.mp3",'rb') as f:
        bot.send_audio(
            chat_id=msg.chat.id,
            audio=f
        )

@bot.message_handler(func=lambda msg:msg.text == "zajia")
def send_multi_message(msg):
    with open(r"D:\telechargements\zajia.jpg",'rb') as f:
        bot.send_photo(
            chat_id=msg.chat.id,
            photo=f
        )
    bot.send_message(
        chat_id=msg.chat.id,
        text="zajia PRODUCT PRIX 199DH"
    )
@bot.edited_message_handler(commands=["noice"])
def send_multi_messages(msg):
    bot.send_message(chat_id=msg.chat.id,text="Wow I saw what you did")

@bot.message_handler(commands=["lol"])
def send_multi_messages(msg):
    bot.send_sticker(
        chat_id=msg.chat.id,
        sticker= 'CAACAgIAAxkBAAOTYlXxlgInffyRRfIWV6IwTpa6N64AAnUTAALMkYlL1w-glB7Evk0jBA',
    )
@bot.message_handler(commands=["irmizahr"])
def send_multi_messages(msg):
    bot.send_dice(
        chat_id=msg.chat.id,
    )
@bot.message_handler(commands=["game"])
def send_multi_messages(msg):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    rbn = types.KeyboardButton("/boo")

bot.polling()
