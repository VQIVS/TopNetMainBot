from telebot import TeleBot, types
from bot.keyboards import keyboard, products_keyboard, ConfirmOrder_keyboard, payment_keyboard
from bot.models import User, Order, Email, Link
import os
import django
from django.db import DatabaseError
import re

products_ids = {
    '⭐️ گروه SILVER': {"link_id": 1, "price": 24},
    '⭐️ گروه GOLD-1': {"link_id": 2, "price": 48},
    '⭐️ گروه GOLD-2': {"link_id": 3, "price": 72},
}
# '⭐️ گروه PLATINUM-2' : {"link_id": 5, "price": 179},
# '⭐️ گروه DIAMOND': {"link_id": 6, "price": 199},
# '⭐️ گروه PLATINUM-1': {"link_id": 4, "price": 159},


bot = TeleBot("6265375073:AAFVb46E6EGkcp5AqcyORKiswf7SSel-rlg")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

django.setup()

user_selected_option = {}


@bot.message_handler(['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, '⚡', reply_markup=keyboard)
    text = "لطفا قبل از خرید با استفاده از دکمه اضافه کردن نام کاربری , نام کاربری خود را اضافه کنید و سپس اقدام به خرید بفرمایید"
    bot.send_message(user_id, text)


@bot.message_handler(func=lambda message: message.text == 'اضافه کردن نام کاربری')
def add_email(message):
    user_id = message.from_user.id
    address = str(user_id) + '@telegram.com'
    user, created = User.objects.get_or_create(user_id=str(user_id))
    user.primary_email = address
    user.save()
    bot.send_message(user_id, "لطفا نام کاربری خود را به صورت صحیح وارد کنید")


@bot.message_handler(func=lambda message: message.text == '⭐️خرید سرویس')
def buy(message):
    user_id = message.from_user.id
    message_buy = """🛒 لطفاً یکی از پلن های زیر را برای خرید انتخاب کنید.
    (اشتراک ها محدودیتی برای تعداد کاربر ندارند.)"""
    bot.send_message(user_id, message_buy, reply_markup=products_keyboard)


@bot.message_handler(func=lambda message: message.text == "💬پشتیبانی")
def support(message):
    user_id = message.from_user.id
    support_message = """🟦برای رفع مشکل اتصال، لطفا هرروز اشتراک خود را مطابق این پست آپدیت کنید: https://t.me/AZUREWebVPN/23
📞برای رفع مشکل یا صحبت با پشتیبانی به آیدی مقابل پیام دهید: @AZUREWebSUPPORT
❎لطفا دقت کنید اسم کانفیگ آخر اشتراکتون بعد از هر بار آپدیت اشتراکتون، حجم و زمان باقیماندتون رو نمایش میدهد.
    """
    bot.send_message(user_id, support_message)


@bot.message_handler(func=lambda message: message.text == "📚راهنما اتصال")
def how_to_connect(message):
    user_id = message.from_user.id
    text = """🟦لطفا هرروز اشتراک خود را مطابق این پست آپدیت کنید: https://t.me/AZUREWebVPN/23
✅برای دانلود نرم افزار، راهنمای وارد کردن لینک و اتصال، مطالب کانال زیر را مشاهده کنید: @RahnamaAZUREWeb
❎لطفا دقت کنید اسم کانفیگ آخر اشتراکتون بعد از هر بار آپدیت اشتراکتون، حجم و زمان باقیماندتون رو نمایش میدهد.
    """
    bot.send_message(user_id, text)


@bot.message_handler(func=lambda message: message.text == "درخواست حجم سفارشی")
def message_chat(message):
    user_id = message.from_user.id
    text = """ برای درخواست ججم دلخواهتان به پشتیبانی پیام دهید:)"""
    bot.send_message(user_id, text)


@bot.callback_query_handler(func=lambda query: query.data in products_ids)
def select_email(query):
    selected_option = query.data
    user_id = query.message.chat.id
    user_selected_option[user_id] = selected_option

    user, created = User.objects.get_or_create(user_id=str(user_id))
    email_addresses = user.emails.all()

    keyboard_email = types.InlineKeyboardMarkup(row_width=1)
    for email in email_addresses:
        button = types.InlineKeyboardButton(text=email.address, callback_data=f"email_{email.id}")
        keyboard_email.add(button)
    bot.send_message(user_id, "ابتدا نام کاربری خود را انتخاب کنید", reply_markup=keyboard_email)


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

    invoice_message = f"فاکتور شما: {selected_option}\n\n" \
                      f"کد کاربری: {user.user_id}\n\n" \
                      f"ایمیل: {selected_email.address}\n\n" \
                      f"قیمت محصول به تومان: {selected_product['price']}\n\n" \
                      f"وضعیت سفارش: {order.status}\n\n" \
                      f"تعداد: {order.quantity}\n\n" \

    bot.send_message(user_id, invoice_message, reply_markup=ConfirmOrder_keyboard)


@bot.callback_query_handler(func=lambda query: query.data == "لغو")
def handler(query):
    user_id = query.message.chat.id
    bot.send_message(user_id, "درخواست شما لغو شد")


def is_valid_username(username):
    username_pattern = r'^[\w\.-]+$'
    return re.match(username_pattern, username)


@bot.message_handler(func=lambda message: is_valid_username(message.text))
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
        message_unsaved = 'نام کاربری تکراری یا اشتباه است.'
        bot.send_message(user_id, message_unsaved)


@bot.callback_query_handler(func=lambda query: query.data == "pay_cart")
def pay_with_card(query):
    user_id = query.message.chat.id
    message_text = """ ❗️عزیزان دقت کنید در صورتی که موقع پرداخت شرح تراکنش نیاز باشد، اگر اشاره ای به خرید VPN انجام بدید، به هیچ عنوان سروری برای شما ارسال نمیشود.

جهت پرداخت از طریق کارت زیر به نام 
محمد مهدی تحویلیان اقدام کنید:

6104337659461683

✅سپس در بات رسید کامل واریز را در بات  ارسال کنید."""
    bot.send_message(user_id, message_text)


@bot.callback_query_handler(func=lambda query: query.data == "بله")
def payment_callback(query):
    user_id = query.message.chat.id
    #     text = """ارز مورد نظر حتما ترون انتخاب شود
    # آدرس دریافتی:
    # TVmk4D6nWWG7Vw2gGKEtu7Sh4NpJ5PaSPQ
    #  در مرحله مقدر ترون، لطفا مقدار ترون اعلام شده توسط ربات را وارد نمایید.
    #
    # ✅در صورتی که خودتان درگاه ارز دیجیتال یا کیف پول میشناسید و استفاده میکنید، میتوانید با استفاده از آن کیف پول واریز نمایید.
    # در غیر این صورت روی گزینه پرداخت کلیک کنید.
    #
    # 🟢️️️️️️پس از پرداخت اسکرین شات رسید خود را داخل بات بفرستید و منتظر باشید تا لینک شما ارسال شود(۵دقیقه تا ۱ ساعت)
    #
    # @top_netvpn 🔥"""

    text = """لطفا نحوه پرداخت خود را مشخص کنید."""
    bot.send_message(user_id, text, reply_markup=payment_keyboard)


@bot.message_handler(content_types=['photo'])
def confirmation(message):
    user_id = message.from_user.id
    messageـbox = "رسید شما دریافت شد.\nمنتظر بمونید تا پرداخت شما تایید بشه :)\nممنون از صبوریتون."
    order = Order.objects.filter(username=user_id).last()
    link_id = order.link_id
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

    bot.reply_to(message, messageـbox)

    admin_channel_id = "-1002112197238"
    with open(local_photo_path, 'rb') as photo_to_send:
        bot.send_photo(admin_channel_id, photo_to_send,
                       caption=f"User {user_id} Payment Confirmation(AZW) for product {link_id}")


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
        order = Order.objects.filter(username=user_id).last()
        print(order)
        if order:
            link_id = order.link_id
            print("link_id", link_id)
            link = Link.objects.filter(link_id=link_id, status=True).first()
            if link:
                message_link = f"""
                با لینک زیر میتونید به اشتراکتون دسترسی پیدا کنید :
                
                {link}
                ❎لطفا دقت کنید اسم کانفیگ اول اشتراکتون بعد از هر بار آپدیت اشتراکتون، حجم و زمان باقیماندتون رو نمایش میدهد.
                
                    🟦برای رفع مشکل اتصال، لطفا هرروز اشتراک خود را مطابق این پست آپدیت کنید: https://t.me/AZUREWebVPN/23
                
                🔴دقت کنید این لینک یک بار برای شما ارسال میشود لطفا لینک را در جای امنی ذخیره کنید(در صورت فقدان لینک, به پشتیبانی پیام بدین.)
                
                """
                link.status = False
                link.save()
                order.status = "Confirmed"
                order.save()
                bot.send_message(user_id, message_link)
            else:
                bot.send_message(user_id, "No valid link found for your order.")
        else:
            bot.send_message(user_id, f"No pending order found for {user_id}.")

# @bot.callback_query_handler(func=lambda query: query.data == 'pay_btn')
# def handle_video(query):
#     chat_id = query.message.chat.id
#     caption = """🟢این روش برای مشتریان جدید و تنها روش پرداختی تاپ نت از طریق ربات می‌باشد.
# مشتری های قدیمی مثل قبل با پیام به اکانت فروش میتوانند خرید کنند.
#
# ⚠️نکته مهمی که‌ هنگام خرید باید به آن‌ توجه کنید این است که مبلغی که از سمت بانک برای شما همراه با رمز دوم اس ام اس میشود با مبلغی که هنگام خرید در سایت نمایش داده میشود یکی باشد⚠️
#
# 🟢تیم تاپ نت هیچگونه مسئولیتی در قبال حمله های فیشینگ و … ندارد و صرفا روش های مختلف پرداخت را برای شما معرفی می‌کند."""
#
#     with open('bot/video_2023-10-05_21-26-24.mp4', 'rb') as video_file:
#         bot.send_video(chat_id, video_file, caption=caption)
