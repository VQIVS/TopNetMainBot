from telebot import TeleBot
from bot.keyboards import keyboard, products_keyboard
from bot.models import User
bot = TeleBot("6635901215:AAEH1u7uqzShEDAm6wBvz1XzsfuD0U69rxs")

@bot.message_handler(['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, '⚡', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == '⭐️خرید سرویس')
def buy(message):
    user_id = message.from_user.id
    message_buy = "🛒 لطفاً یکی از پلن های زیر را برای خرید انتخاب کنید."
    bot.send_message(user_id, message_buy, reply_markup=products_keyboard)


@bot.message_handler(func=lambda message: message.text == "💬پشتیبانی")
def support(message):
    user_id = message.from_user.id
    support_message = "support"
    bot.send_message(user_id, support_message)


product_ids = {
    '⚪️ نقره‌ای 1 : یک ماهه 25GB': 1,
    '⚪️ نقره‌ای 2 : یک ماهه 50GB': 2,
    '⚪️ نقره‌ای 3 : یک ماهه 75GB': 3,
    '🟡 طلایی 4 : یک ماهه 100GB': 4
}
@bot.callback_query_handler(func=lambda query: query.data in product_ids)
def invoice(query):
    user_id = query.message.chat.id
    bot.send_message(user_id, 'لطفا یک ایمیل موجود ارسال کنید')
    user_text = query.text
    user_input = User(user_id=user_id, email=user_text)
    user_input.save()
    bot.send_message(user_id, 'دریافت شد')







