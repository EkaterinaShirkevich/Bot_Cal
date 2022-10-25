from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
import logging
#from Info import Token
import excep as ex
import logg
import compl
import json

Token = '5645070358:AAHTJADMoQkedNwWP-48e11juNrBZYinHVI'


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

TYPE, ACTION, GIVE_NUM, RESULT, MENU = range(5)

type_num = None
action = None


def start(update, _):
    reply_keyboard = [['Начнем']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(f'Приветствую {update.effective_user.first_name}! \n'
                              'Меня зовут Профессор-Калькулятор. Я могу посчитать твой пример \n'
                              'Команда /cancel, чтобы прекратить разговор.\n\n'
                              'Начнем?',
                              reply_markup=markup_key,)
    return TYPE


def type_command(update, _):
    global type_num
    user = update.message.from_user
    logger.info("Start", user.first_name, update.message.text)
    update.message.reply_text(f'Выбери с какими числами хочешь работать?\n\n'
                              '1.Рациональными \n'
                              '2.Комплексными')
    return ACTION


def action_num(update, _):
    global action, type_num
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пол пользователя
    logger.info("Числа %s: %s", user.first_name, update.message.text)
    type_num = update.message.text
    type_num = int(type_num)
    update.message.reply_text(f'Выбери дейстиве или /return чтобы вернуться\n\n'
                              'Сложение: "+"\n'
                              'Вычитание: "-"\n'
                              'Умножение: "*"\n'
                              'Деление: "/"'
                              )
    #action = update.message.text
    return GIVE_NUM


def give_num(update, _):
    global type_num, action
    user = update.message.from_user
    logger.info("Действие %s: %s", user.first_name, update.message.text)
    action = update.message.text
    if action == '/return':
        update.message.reply_text(
        'Ну, ладно. Можешь перевыбрать, или /cancel если хочешь завершить работу.'
        f'Выбери с какими числами хочешь работать?\n\n'
                              '1.Рациональными \n'
                              '2.Комплексными')
        return ACTION
    elif action != '/return':
        if type_num == 1:
            update.message.reply_text('Введите 2 числа через пробел: ')
        elif type_num == 2:
            update.message.reply_text('Введите 4 числа через пробел: ')
        return RESULT


def res(update, _):
    reply_keyboard = [['Продолжить']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    global type_num, action, num1
    user = update.message.from_user
    logger.info("Действие %s: %s", user.first_name, update.message.text)
    if type_num == 1:
        num1 = update.message.text
        num1 = num1.replace(' ', action)
        update.message.reply_text(f'{num1}={round(eval(num1))}', reply_markup=markup_key,)

    elif type_num == 2:
        num1 = update.message.text
        k = compl.cal_compl(num1, action)
        print(k)
        update.message.reply_text(f'{k}',reply_markup=markup_key,)
                                  #reply_markup=ReplyKeyboardRemove())
    return MENU


def menu(update, _):
    user = update.message.from_user
    logger.info("Ответ бота: %s. Пользователь", user.first_name,"Ждет указаний")
    reply_keyboard = [['Начнем']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Чтобы снова посчитать /start\n'
        'Хочешь завершить работу /cancel\n\n'
        'Твои действия?'
    )
    if update.message.from_user == '/start':
        update.message.reply_text(f'Я могу посчитать еще \n'
                              'Команда /cancel, чтобы прекратить разговор.\n\n'
                              'Начнем?',
                              reply_markup=markup_key,)
        return CommandHandler('start', type_command)
    else:
        return CommandHandler('cancel', cancel)


def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s не хочет.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.'
        # reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(Token)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            TYPE: [MessageHandler(Filters.regex('^(Начнем)$'), type_command)],
            ACTION: [MessageHandler(Filters.text, action_num)],
            # , CommandHandler('return', return_type)],
            GIVE_NUM: [MessageHandler(Filters.text, give_num)],
            RESULT: [MessageHandler(Filters.text, res)],
            MENU: [MessageHandler(Filters.text, menu)]
            # , CommandHandler('return', return_type)]
        },

        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()
