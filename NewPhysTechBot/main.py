import telebot
from telebot import types

bot=telebot.TeleBot('6159680530:AAHhyp72GrNF7fOfF7TBRn0RcM-8NGwvBhg')

#creating a button

# @bot.message_handler(commands = ['start'])
# def url(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton(text='Новый Физтех ИТМО', url='https://physics.itmo.ru/en')
#     markup.add(btn1)
#     bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт Нового Физтеха ИТМО", reply_markup = markup)
#

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помощник по всему, что связано с Новым Физтехом ИТМО!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Узнать расписание Нового Физтеха ИТМО')
        btn2 = types.KeyboardButton('Печать документов')
        btn3 = types.KeyboardButton('Wiki Нового Физтеха')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Выберите интересующую вас опцию', reply_markup=markup) #ответ бота
    elif message.text == 'Узнать расписание Нового Физтеха ИТМО':
        bot.send_message(message.from_user.id, 'Для того, чтобы посмотреть расписание, перейдите по '+'[ссылке](https://docs.google.com/spreadsheets/d/1w1nIVkxW2ibAPV_BCkV3-B8czREx_1fN5lmTyl9XkJQ/edit#gid=1941185286)', parse_mode='Markdown')
    elif message.text == 'Печать документов':
        bot.send_message(message.from_user.id, 'Эта опция пока ещё не реализована, но скоро мы это исправим)')
    elif message.text == 'Wiki Нового Физтеха':
        bot.send_message(message.from_user.id, 'Для того, чтобы попасть на Wiki Нового Физтеха, перейдите по '+ '[ссылке](https://wiki.physics.itmo.ru/Main_Page)', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0)