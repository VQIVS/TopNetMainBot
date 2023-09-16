from telebot import types

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons_row1 = [
    types.KeyboardButton('⭐️خرید سرویس'),
]
buttons_row2 = [
    types.KeyboardButton('لینک اتصال 🔗'),
    types.KeyboardButton('💬پشتیبانی'),

]
buttons_row3 = [
    types.KeyboardButton('📚راهنما اتصال'),
    types.KeyboardButton('سوالات متداول'),
]
buttons_row4 = [
    types.KeyboardButton('🛍 خرید عمده'),
]
keyboard.add(*buttons_row1)
keyboard.add(*buttons_row2)
keyboard.add(*buttons_row3)
keyboard.add(*buttons_row4)

# FAQZ_keyboard = types.InlineKeyboardMarkup(row_width=1)
# button = types.InlineKeyboardButton("تایید", callback_data="تایید")
# FAQZ_keyboard.add(button)

products_keyboard = types.InlineKeyboardMarkup(row_width=1)
product_1 = types.InlineKeyboardButton('⚪️ نقره‌ای 1 : یک ماهه 25GB', callback_data='⚪️ نقره‌ای 1 : یک ماهه 25GB')
product_2 = types.InlineKeyboardButton('⚪️ نقره‌ای 2 : یک ماهه 50GB', callback_data='⚪️ نقره‌ای 2 : یک ماهه 50GB')
product_3 = types.InlineKeyboardButton('⚪️ نقره‌ای 3 : یک ماهه 75GB', callback_data='⚪️ نقره‌ای 1 : یک ماهه 75GB')
product_4 = types.InlineKeyboardButton('🟡 طلایی 4 : یک ماهه 100GB', callback_data='🟡 طلایی 2 : یک ماهه 100GB')
products_keyboard.add(product_1, product_2, product_3, product_4)

invoice_keyboard = types.InlineKeyboardMarkup(row_width=1)
yes_btn = types.InlineKeyboardButton("بله", callback_data="بله")
no_btn = types.InlineKeyboardButton("لفو", callback_data="لفو")
invoice_keyboard.add(yes_btn, no_btn)


