import telebot
import random

token = "6561323271:AAEljREUDPmbHhmNIvN7wlRxNxUdr5ByQms"

bot = telebot.TeleBot(token)
my_list = ["hi", "hello", "good", "bad", "day", "night", "lesson", "python", "year", "month"]
"""
def func(message):
    return message.text.lower()== "how are you?"

@bot.message_handler(func = func)
def random_message(message):
    rand_answer = random.choice(my_list)
    bot.reply_to(message, rand_answer)

"""    
@bot.message_handler(func = lambda message: message.text.lower() == "how are you?")
def random_message(message):
    rand_answer = random.choice(my_list)
    bot.reply_to(message, rand_answer)

bot.infinity_polling()


# bot which answers on "how are you?" with random answer. It should understand both lowercase and uppercase letters.