import telebot
import random

token = ""

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
