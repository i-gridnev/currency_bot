import telebot, re
from telebot import types
from currency import show_currency

token = '5315727355:AAEl2lovWYamspstYgvKCI8c50esSGzxhgw'

bot = telebot.TeleBot(token)
currencies_flag_list = ['USD 🇺🇸', 'RUB 🇷🇺', 'UAH 🇺🇦', 'AUD 🇦🇺', 'CNY 🇨🇳', 'EUR 🇪🇺']
currencies_list = ['USD', 'RUB', 'UAH', 'AUD', 'EUR']
crypto_list = ['BTC', 'ETH', 'LTC', 'CZK', 'XLM', 'BNB']
all_currencies = currencies_list + crypto_list
start_menu_list = ['Crypto 💎', 'Currency 🏦']

rule = '\d\s[A-Z, a-z]{3}'


def menu(menu_list: list):
    markup = types.ReplyKeyboardMarkup()
    buttons = [types.KeyboardButton(b) for b in menu_list]
    markup.add(*buttons)
    return markup


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = menu(menu_list=start_menu_list)
    bot.send_message(message.chat.id, '🖖 Здарова! Выбирай че нада👇', reply_markup=markup)
    bot.send_message(message.chat.id, 'Либо напиши число и валюту: "2 btc"')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text in start_menu_list and message.text == 'Currency 🏦':
        menu_w = currencies_list.copy()
        menu_w.append('Назад ↩')
        markup = menu(menu_list=menu_w)
        bot.send_message(message.chat.id, 'Выбери валюту 💰', reply_markup=markup)

    elif message.text in start_menu_list and message.text == 'Crypto 💎':
        menu_w = crypto_list.copy()
        menu_w.append('Назад ↩')
        markup = menu(menu_list=menu_w)
        bot.send_message(message.chat.id, 'Выбери валюту 💰', reply_markup=markup)

    elif message.text == 'Назад ↩':
        markup = menu(menu_list=start_menu_list)
        bot.send_message(message.chat.id, 'Выбирай че нада👇', reply_markup=markup)

    elif message.text in crypto_list:
        bot.reply_to(message, show_currency(message.text, currencies_list))

    elif message.text in currencies_list:
        bot.reply_to(message, show_currency(message.text, currencies_list))

    elif bool(re.search(rule, message.text)):
        base = ''.join(message.text.split()[1:])
        bot.reply_to(message, show_currency(base.upper(), currencies_list, int(''.join(message.text.split()[:1]))))

    else:
        bot.reply_to(message, 'Моя не понимать 🤷‍♂')


bot.infinity_polling()

# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     markup = show_buttons(currencies)
#     if call.message:
#         if call.data == 'USD 🇺🇸':
#             bot.edit_message_text(chat_id = call.message.chat.id,
#                                   message_id= call.message.id,  text= 'Money!', reply_markup=markup)
#         elif call.data == 'question2':
#             bot.send_message(call.message.chat.id, 'Ну и вали!!', reply_markup=markup)
