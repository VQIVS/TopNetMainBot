import json

from telebot import TeleBot, types
from bot.keyboards import keyboard, products_keyboard, ConfirmOrder_keyboard, payment_keyboard
from bot.models import User, Order, Email, Link
import os
import django
from django.db import DatabaseError
import re


products_ids = {
    '⭐️ گروه SILVER': {"link_id": 1, "price": 19},
    '⭐️ گروه GOLD-1': {"link_id": 2, "price": 29},
    '⭐️ گروه GOLD-2': {"link_id": 3, "price": 34},
    '⭐️ گروه PLATINUM-1': {"link_id": 4, "price": 38},
    '⭐️ گروه PLATINUM-2': {"link_id": 5, "price": 43},
    '⭐️ گروه DIAMOND': {"link_id": 6, "price": 48},
}

bot = TeleBot("6635901215:AAEH1u7uqzShEDAm6wBvz1XzsfuD0U69rxs")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

django.setup()

user_selected_option = {}

@bot.message_handler(['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, '⚡', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'اضافه کردن ایمیل')
def add_email(message):
    user_id = message.from_user.id
    address = str(user_id) + '@telegram.com'
    user, created = User.objects.get_or_create(user_id=str(user_id))
    user.primary_email = address
    user.save()
    bot.send_message(user_id, "Please send your email address:")


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


@bot.callback_query_handler(func=lambda query: query.data in products_ids)
def select_email(query):
    selected_option = query.data
    user_id = query.message.chat.id
    user_selected_option[user_id] = selected_option

    user, created = User.objects.get_or_create(user_id=str(user_id))

    bot.send_message(user_id, "Please select an email address for the order:")

    email_addresses = user.emails.all()

    keyboard_email = types.InlineKeyboardMarkup(row_width=1)
    for email in email_addresses:
        button = types.InlineKeyboardButton(text=email.address, callback_data=f"email_{email.id}")
        keyboard_email.add(button)
    bot.send_message(user_id, "Select an email address:", reply_markup=keyboard_email)


@bot.callback_query_handler(func=lambda query: query.data.startswith("email_"))
def invoice(query):
    user_id = query.message.chat.id
    selected_email_id = int(query.data.split("_")[1])

    user = User.objects.get(user_id=str(user_id))
    selected_option = user_selected_option.get(user_id)

    if not selected_option:
        bot.send_message(user_id, "Please select a product first.")
        return

    selected_email = Email.objects.get(id=selected_email_id)

    if selected_option not in products_ids:
        bot.send_message(user_id, "Invalid product selection.")
        return

    selected_product = products_ids[selected_option]

    order = Order.objects.create(
        user_id=user,
        username=user_id,
        link_id=selected_product["link_id"],
        email=selected_email,
        status="Pending",
        quantity=1,
    )

    invoice_message = f"فاکتور شما: {selected_option}\n" \
                      f"کد کاربری: {user.user_id}\n" \
                      f"ایمیل: {selected_email.address}\n" \
                      f"قیمت محصول: {selected_product['price']}\n" \
                      f"وضعیت سفارش: {order.status}\n" \
                      f"تعداد: {order.quantity}"

    bot.send_message(user_id, invoice_message, reply_markup=ConfirmOrder_keyboard)


@bot.callback_query_handler(func=lambda query: query.data == "لغو")
def handler(query):
    user_id = query.message.chat.id
    bot.send_message(user_id, "درخواست شما لغو شد")

def is_valid_email(email):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_pattern, email)


@bot.message_handler(func=lambda message: is_valid_email(message.text))
def handler(message):
    user_id = message.chat.id
    email = message.text
    try:
        user, created = User.objects.get_or_create(user_id=str(user_id))

        email_obj, created = Email.objects.get_or_create(address=email)
        user.emails.add(email_obj)

        message_save = f'کاربر {email} ثبت شد'
        bot.send_message(user_id, message_save)
    except DatabaseError:
        message_unsaved = 'ایمیل تکراری است.'
        bot.send_message(user_id, message_unsaved)


@bot.message_handler(func=lambda query: query.data == "پرداخت")
def payment_handler(query):
    pass

@bot.callback_query_handler(func=lambda query: query.data == "بله")
def payment_callback(query):
    user_id = query.message.chat.id
    text = """ارز مورد نظر حتما ترون انتخاب شود
آدرس دریافتی: 
TVmk4D6nWWG7Vw2gGKEtu7Sh4NpJ5PaSPQ
 در مرحله مقدر ترون، لطفا مقدار درون اعلام شده توسط ربات را وارد نمایید.

✅در صورتی که خودتان درگاه ارز دیجیتال یا کیف پول میشناسید و استفاده میکنید، میتوانید با استفاده از آن کیف پول واریز نمایید.

🟢این روش برای مشتریان جدید و تنها روش پرداختی تاپ نت از طریق ربات می‌باشد.
مشتری های قدیمی مثل قبل با پیام به اکانت فروش میتوانند خرید کنند.

⚠️نکته مهمی که‌ هنگام خرید باید به آن‌ توجه کنید این است که مبلغی که از سمت بانک برای شما همراه با رمز دوم اس ام اس میشود با مبلغی که هنگام خرید در سایت نمایش داده میشود یکی باشد⚠️

🟢تیم تاپ نت هیچگونه مسئولیتی در قبال حمله های فیشینگ و … ندارد و صرفا روش های مختلف پرداخت را برای شما معرفی می‌کند.
@top_netvpn 🔥"""
    bot.send_message(user_id, text, reply_markup=payment_keyboard)

@bot.message_handler(content_types=['photo'])
def confirmation(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    reply_message = "Thank you for sending the payment confirmation. We will verify it shortly."
    save_directory = "bot/receipts/img"
    photo = message.photo[-1]
    file_id = photo.file_id
    file_info = bot.get_file(file_id)
    file_extension = os.path.splitext(file_info.file_path)[-1]
    unique_filename = f"photo_{file_id}{file_extension}"
    local_photo_path = os.path.join(save_directory, unique_filename)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(local_photo_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.reply_to(message, reply_message)

    admin_channel_id = "-1001951490996"
    with open(local_photo_path, 'rb') as photo_to_send:
        bot.send_photo(admin_channel_id, photo_to_send, caption=f"User {user_id} Payment Confirmation")


def extract_user_id_from_caption(caption):
    parts = [part.strip() for part in caption.split(' ')]
    user_id = int(parts[1])
    return user_id

@bot.channel_post_handler(content_types=['text'])
def handle_channel_post(message):
    if "confirm" in message.text.lower() and message.reply_to_message:
        user_id = extract_user_id_from_caption(message.reply_to_message.caption)
        print(user_id)
        print(type(user_id))
        order = Order.objects.filter(username=user_id).first()
        print(order)
        if order:
            link_id = order.link_id
            link = Link.objects.filter(link_id=link_id, status=True).first()
            if link:
                link_text = f"Here is your download link: {link.link}"
                link.status = False
                link.save()
                bot.send_message(user_id, link_text)
            else:
                bot.send_message(user_id, "No valid link found for your order.")
        else:
            bot.send_message(user_id, f"No pending order found for {user_id}.")













