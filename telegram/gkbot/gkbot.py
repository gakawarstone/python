import telebot
import config
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot(config.token)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text)
    answ(message)
    if message.text == '/sqr':
        bot.send_message(message.chat.id, "Возведение в квадрат:")
        bot.register_next_step_handler(message, sqr)
    if message.text == '/syst':
        bot.send_message(message.chat.id, "Система счисления:")
        bot.register_next_step_handler(message, syst_number)


def answ(message):
    dict = {
        'Пидор': 'Сам пидор',
        'пидор': 'Сам пидор',

        'Зря быканул': 'Согласен',
        'зря быканул': 'Согласен',

        'Кто?': 'Ты',
        'кто?': 'ты',
        'Я?': 'Да, ты',
        'я?': 'да, ты',
        'Что?': 'Ну ты',
        'что?': 'ну ты',
        'Что я?': 'Ну кто?',
        'что я?': 'ну кто?',
        'Я - ты': 'А я?',
        'я - ты': 'а я?',
        'Ты - я': 'Пожалуй, соглашусь',
        'ты -я': 'пожалуй, соглашусь',
    }
    if message.text in dict:
        bot.send_message(message.chat.id, dict[message.text])


def sqr(message):
    global number
    number = 0
    try:
        number = int(message.text)
        bot.send_message(message.chat.id, str(int(number) ** 2))
    except Exception:
        bot.send_message(message.chat.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, sqr)


def syst_number(message):
    global n
    try:
        n = int(message.text)
        bot.send_message(message.chat.id, 'Число в десятичной системе счиления которое нужно перевести:')
        bot.register_next_step_handler(message, syst)
    except Exception:
        bot.send_message(message.chat.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, syst_number)


def conNS(x, si1, si2):
    b = ''
    b += str(x % si2)
    while x >= si2:  # Пока не закончится остаток
        x = x//si2
        b += str(x % si2)
    return b[::-1]


def syst(message):
    outp = ''
    syst = n
    try:
        x = int(message.text)
        outp = conNS(x, 10, syst)
        bot.send_message(message.chat.id, outp)
    except Exception:
        bot.send_message(message.chat.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, syst)


bot.polling(none_stop=True, interval=0)
