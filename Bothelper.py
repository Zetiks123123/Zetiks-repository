from telebot import TeleBot



bot = TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Chek my repository https://github.com/Zetiks123123/Zetiks-repository')


@bot.message_handler(commands=['Weather'])
def start(message):
    bot.send_message(message.chat.id, 'https://yandex.ru/pogoda/moscow?ysclid=m9o61nz24o54534615')

bot.infinity_polling()
