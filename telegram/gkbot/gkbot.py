import telebot
bot = telebot.TeleBot('1159177907:AAHJLhyVsJ3ZgT5ZX7k2aWz7uEK_oBYT9NA')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    answ(message, 'Пидор', 'Сам пидор')
    answ(message, '1', '2')
    if message.text == '/sqr':
        bot.register_next_step_handler(message, sqr)


def answ(message, q, a):
    if message.text == q:
        bot.send_message(message.chat.id, a)


def sqr(message):
    number = message.text
    bot.send_message(message.chat.id, "Возведение в квадрат:")
    bot.send_message(message.chat.id, str(int(number) ** 2))


bot.polling(none_stop=True, interval=0)
