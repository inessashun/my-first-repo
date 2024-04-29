import telebot    # library to work with Telegram
import datetime   # module to work with date and time
import time       # to hold program
import threading  # to work with flow
import random

bot = telebot.TeleBot("7190148247:AAFicu5jRorhQdF9HnoJHua91yBcqdTU3Rw")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Hello, I am a chatbot to remind you to drink a water')
    reminder_thread = threading.Thread(target=send_reminders, args = (message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['fact'])
def start_message(message):
    list = ["**One factor in estimating when water appeared on Earth is that water is continually being lost to space.",
            "**When the Earth was younger and less massive, water would have been lost to space more easily."]
    random_fact = random.choice(list)
    bot.reply_to(message, f'Look the fact about water {random_fact}')
def send_reminders(chat_id):
    first_rem = "10:00"
    second_rem = "15:00"
    third_rem = "20:00"
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem or now == second_rem or now == third_rem:
            bot.send_message(chat_id, "Reminder, now is the time to drink a water")
            time.sleep(61)
        time.sleep(1)

bot.polling(none_stop=True)

