from telebot import TeleBot
from keyboards import keyboard

bot = TeleBot("6635901215:AAEH1u7uqzShEDAm6wBvz1XzsfuD0U69rxs")

bot.message_handler(commands=['start'])


def start(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, '⚡', reply_markup=keyboard)


