from telebot import types
from telebot.types import InlineKeyboardMarkup

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons_row1 = [
    types.KeyboardButton('⭐️خرید سرویس'),
]
buttons_row2 = [
    types.KeyboardButton('💬پشتیبانی'),
    types.KeyboardButton('📚راهنما اتصال'),

]
buttons_row3 = [
    types.KeyboardButton('اضافه کردن ایمیل'),
]
keyboard.add(*buttons_row1)
keyboard.add(*buttons_row2)
keyboard.add(*buttons_row3)

products_keyboard = types.InlineKeyboardMarkup(row_width=1)
product_1 = types.InlineKeyboardButton('1 کاربر |📆 مدت: 30 روز |‌🔵 30 گیگابایت |‌ 94 هزار تومان (17ترون)', callback_data='⭐️ گروه SILVER')
product_2 = types.InlineKeyboardButton('1 کاربر |📆 مدت: 30 روز |‌🔵 60 گیگابایت |‌ 134 هزار تومان (26ترون)', callback_data='⭐️ گروه GOLD-1')
product_3 = types.InlineKeyboardButton('2 کاربر |📆 مدت: 30 روز |‌🔵 60 گیگابایت |‌ 154 هزار تومان (31ترون)', callback_data='⭐️ گروه GOLD-2')
product_4 = types.InlineKeyboardButton('3 کاربر |📆 مدت: 30 روز |‌🔵 90 گیگابایت |‌ 174 هزار تومان (35ترون)', callback_data='⭐️ گروه PLATINUM-1')
product_5 = types.InlineKeyboardButton('4 کاربر |📆 مدت: 30 روز |‌🔵 120 گیگابایت |‌ 214 هزار تومان (44ترون)', callback_data='⭐️ گروه PLATINUM-2')
product_6 = types.InlineKeyboardButton('1 کاربر |📆 مدت: 30 روز |‌🔵 حجم نامحدود  |‌ 314 هزار تومان (66ترون)', callback_data='⭐️ گروه DIAMOND')
products_keyboard.add(product_1, product_2, product_3, product_4, product_5, product_6)

ConfirmOrder_keyboard = types.InlineKeyboardMarkup(row_width=2)
yes_btn = types.InlineKeyboardButton("بله", callback_data="بله")
no_btn = types.InlineKeyboardButton("لفو", callback_data="لفو")
ConfirmOrder_keyboard.add(yes_btn, no_btn)

payment_keyboard = types.InlineKeyboardMarkup(row_width=1)
pay_button = types.InlineKeyboardButton('پرداخت', callback_data="pay", url="https://t.me/Feenonetbot")
how_to_pay_button = types.InlineKeyboardButton('نحوه پرداخت', callback_data="pay_btn", url="https://t.me/PardakhtFinonet/3")
payment_keyboard.add(pay_button, how_to_pay_button)








