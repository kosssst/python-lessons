import telebot

token = ""

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help', 'start'])
def hi_message(message):
    print(message.text)

bot.infinity_polling()


# bot which answers on "how are you?" with random answer. It should understand both lowercase and uppercase letters.