from telebot import TeleBot
from bot.keyboards import keyboard, products_keyboard, ConfirmOrder_keyboard, payment_keyboard
from bot.models import User
import os
import django
from django.db import transaction, DatabaseError
from django.http import HttpResponse
import requests

api_key = "930014174178211766447672"
recipient_wallet = "recipient_wallet_address"
api_endpoint = 'https://mrswap.org/wallp/custom.php'


products_prices = {
    "product_1": 100,
    "product_2": 200,
    "product_3": 300,
    "product_4": 400,
}

bot = TeleBot("6635901215:AAEH1u7uqzShEDAm6wBvz1XzsfuD0U69rxs")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

django.setup()


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
    selected_option = query.data
    invoice_message = f" پلن انتخابی شما : {selected_option} "
    bot.send_message(user_id, invoice_message, reply_markup=ConfirmOrder_keyboard)


@bot.callback_query_handler(func=lambda query: query.data == "لغو")
def handler(query):
    user_id = query.message.chat.id
    bot.send_message(user_id, "درخواست شما لغو شد")


@bot.callback_query_handler(func=lambda query: query.data == "بله")
def handler(query):
    user_id = query.message.chat.id
    bot.send_message(user_id, "لطفا یک ایمیل معتبر یا نام کاربری دلخواه وارد کنید(نام کاربری به حروف لاتین باشد)")
    pass


@bot.message_handler(func=lambda message: True)
def handler(message):
    user_id = message.chat.id
    email = message.text
    try:
        email = User(user_id=user_id, email=email)
        with transaction.atomic():
            email.save()
            message_save = f'کاربر  {email}ثبت شد'
            message_pay = "برای پرداخت دکمه پایین رو لمس کنید"
            bot.send_message(user_id, message_save)
            bot.send_message(user_id, message_pay, reply_markup=payment_keyboard)
    except DatabaseError:
        message_unsaved = "ایمیل یا نام کاربری تکراری یا نامعتبر است لطفا محصول را دوباره انتخاب کرده و ایمیل یا نام " \
                          "کاربری معتبر وارد کنید(حتما با حروف لاتین باشد)"
        bot.send_message(user_id, message_unsaved)
        return HttpResponse(Exception)


@bot.message_handler(func=lambda query: query.data == "product_1")
def handle_product_selection(query):
    product_price = query.data
    user_id = query.message.chat.id

    # Calculate the total amount based on the selected product
    total_amount = products_prices[product_price]

    # Create a dictionary with the required parameters
    data = {
        'key': api_key,
        'wallet': recipient_wallet,
        'amount': total_amount
    }

    response = requests.post(api_endpoint, data=data)
    print("response")


