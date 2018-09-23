import telebot
import constants
import datetime

bot = telebot.TeleBot(constants.token)
Sbot = telebot.TeleBot(constants.STGV_token)
dw = datetime.datetime.today().weekday()

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id,"Добро пожаловать!")
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('/расписание')
    user_markup.row('/воспетка')
    user_markup.row('/дежурные')
    bot.send_message(message.from_user.id, "Чем могу помочь?", reply_markup=user_markup)
    Sbot.send_message(constants.GV, "Команда /start")
    print("Команда /start")

@bot.message_handler(commands=['расписание'])
def handle_rasp(message):
    if dw == 6:
        bot.send_message(message.from_user.id,'Не учимся мы сегодня, одаренный!')
        bot.send_message(message.from_user.id, 'Завтра:\n'
                                               '1. Биология \n'
                                               '2. Физика \n'
                                               '3. Английский язык \n'
                                               '4. Алгебра \n'
                                               '5. Информатика \n'
                                               '6. Информатика')
    elif dw == 0:
        bot.send_message(message.from_user.id, '1. Биология \n'
                                               '2. Физика \n'
                                               '3. Английский язык \n'
                                               '4. Алгебра \n'
                                               '5. Информатика \n'
                                               '6. Информатика')
    elif dw == 1:
        bot.send_message(message.from_user.id, '1. Физика \n'
                                               '2. Всеобщая история \n'
                                               '3. Физкультура \n'
                                               '4. Алгебра \n'
                                               '5. Мат. информатика \n'
                                               '6. Мат. информатика')
    elif dw == 2:
            bot.send_message(message.from_user.id, '1. Алгебра \n'
                                               '2. Английский язык \n'
                                               '3. Информатика \n'
                                               '4. Информатика \n'
                                               '5. Физика \n'
                                               '6. С.К. математика \n'
                                                '7. ОБЖ')
    elif dw == 3:
        bot.send_message(message.from_user.id, "1. Литература \n"
                                               "2. Алгебра \n"
                                               "3. Физкультура \n"
                                               "4. Геометрия \n"
                                               "5. Геометрия \n"
                                               "6. География ")
    elif dw == 4:
        bot.send_message(message.from_user.id, "1. Литература \n"
                                               "2. История России\n"
                                               "3. Физика\n"
                                               "4. Астрономия\n"
                                               "5. Русский язык\n"
                                               "6. Физика")
    elif dw == 5:
        bot.send_message(message.from_user.id, "1. Физкультура\n"
                                               "2. Обществознание\n"
                                               "3. Английский язык\n"
                                               "4. Обществознание\n"
                                               "5. Химия\n"
                                               "6. Литература")
    Sbot.send_message(constants.GV, "Команда /расписание")
    print("Команда /расписание")

@bot.message_handler(commands=['воспетка'])
def handle_vosp(message):
    now = datetime.datetime.now()
    then = datetime.datetime(2018, 9, 21)
    delta = now - then
    vosp = delta.days % 3
    if vosp == 0:
        bot.send_message(message.from_user.id, "Ревизор")
    elif vosp == 1:
        bot.send_message(message.from_user.id, "FACE")
    elif vosp == 2:
        bot.send_message(message.from_user.id, "Проблемная")
    Sbot.send_message(message.from_user.id, "Команда /воспетка")
    print("Команда /воспетка")

@bot.message_handler(commands=['дежурные'])
def handle_rasp(message):
    if dw == 0:
        bot.send_message(message.from_user.id,"907")
    elif dw == 1:
        bot.send_message(message.from_user.id,"908")
    elif dw == 2:
        bot.send_message(message.from_user.id,"909")
    elif dw == 3:
        bot.send_message(message.from_user.id,"910")
    elif dw == 4:
        bot.send_message(message.from_user.id,"911")
    elif dw == 5:
        bot.send_message(message.from_user.id,'912')
    elif dw == 6:
        bot.send_message(message.from_user.id, 'Не учимся мы сегодня, одаренный!')
        bot.send_message(message.from_user.id, "Завтра 907")
    Sbot.send_message(constants.GV, "Команда /дежурные")
    print("Команда /дежурные")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.from_user.id, "/расписание - Расписание на день\n"
                                           "/воспетка - Сегоднящний ночной воспитатель\n"
                                           "/дежурные - сегодняшняя дежурная комната")
    Sbot.send_message(constants.GV, "Команда /help")
    print("Команда /help")

#CЛЕЖКА
@bot.message_handler(content_types=['text'])
def handle_message(message):
    mfu = message.text
    Sbot.send_message(constants.GV,"От: "+ message.from_user.first_name + " " + "\n"  + mfu)
    bot.send_message(constants.GV, "Ойтушник не знает что такое " + mfu)
    print("От: "+ message.from_user.first_name + " " + "\n"  + mfu)

bot.polling(none_stop=True, interval=0)