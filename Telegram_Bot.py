
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
import logging
from Info import Token
import logg
import compl


Token = Token()


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
    logg.entered_logger(user.first_name, update.message.text)
    update.message.reply_text(f'Выбери с какими числами хочешь работать?\n\n'
                              '1.Рациональными \n'
                              '2.Комплексными')
    return ACTION


def action_num(update, _):
    global action, type_num
    user = update.message.from_user
    logg.entered_logger(user.first_name, update.message.text)
    type_num = update.message.text
    if type_num != '1' and type_num != '2':
        update.message.reply_text('Такого пункта нет в списке.\n'
                                  'Попробуй еще раз.\n'
                                  f'Выбери с какими числами хочешь работать?\n\n'
                                  '1.Рациональными \n'
                                  '2.Комплексными')
        logg.actions_logger(
            'Введено некорректное значение при выборе типов чисел')
        return ACTION
    else:
        update.message.reply_text(f'Выбери дейстиве или /return чтобы вернуться\n\n'
                                  'Сложение: "+"\n'
                                  'Вычитание: "-"\n'
                                  'Умножение: "*"\n'
                                  'Деление: "/"'
                                  )
        return GIVE_NUM


def give_num(update, _):
    global type_num, action
    user = update.message.from_user
    logg.entered_logger(user.first_name, update.message.text)
    action = update.message.text
    if action == '/return':
        update.message.reply_text(
            'Ну, ладно. Можешь перевыбрать\n'
            f'Выбери с какими числами хочешь работать?\n\n'
            '1.Рациональными \n'
            '2.Комплексными')
        return ACTION
    elif action == '+' or action == '-' or action == '*' or action == '/':
        if type_num == '1':
            update.message.reply_text('Введи 2 числа через пробел: ')
        elif type_num == '2':
            update.message.reply_text('Введи 4 числа через пробел: ')
        return RESULT
    else:
        update.message.reply_text('Такого пункта нет в списке.\n'
                                  'Попробуй еще раз.\n'
                                  'Выбери действие или /return чтобы вернуться\n\n'
                                  'Сложение: "+"\n'
                                  'Вычитание: "-"\n'
                                  'Умножение: "*"\n'
                                  'Деление: "/"'
                                  )
        logg.actions_logger(
            'Введено некорректное значение при выборе операций')
        return GIVE_NUM


def res(update, _):
    reply_keyboard = [['Продолжить'], ['Завершить']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    global type_num, action, num1
    user = update.message.from_user
    logg.entered_logger(user.first_name, update.message.text)
    num1 = update.message.text
    k = num1.replace('.', '').replace(' ', '')
    lsk = num1.split()
    if k.isdigit() and len(lsk) >= 2:
        if type_num == '1' and len(lsk) == 2:
            if lsk[1] == '0' and action == '/':
                update.message.reply_text('Извини, но на ноль делить не умею.\n'
                                          'Введи числа через пробел: ')
                logg.actions_logger('Попытка деления на ноль')
                return RESULT
            else:
                num1 = num1.replace(' ', action)
                res1 = round(eval(num1), 3)
                update.message.reply_text(f'Лови результат: {num1}={res1}\n\n'
                                          'Может еще примерчик?\n\n '
                                          'Твои действия?', reply_markup=markup_key)
                logg.result_logger(res1)  # логгер для результата
                return MENU

        elif type_num == '2' and len(lsk) == 4:
            if lsk[2] == '0' and lsk[3] == '0' and action == '/':
                update.message.reply_text('Извини, но на ноль делить не умею.\n'
                                          'Введи числа через пробел: ')
                logg.actions_logger('Попытка деления на ноль')
                return RESULT
            else:
                res1 = compl.cal_compl(num1, action)
                update.message.reply_text(f'Лови результат: {res1}\n\n'
                                          'Может, еще примерчик?\n\n '
                                          'Твои действия?', reply_markup=markup_key)
                logg.result_logger(res1)  # логгер для результата
                return MENU
        else:
            if type_num == '1':
                update.message.reply_text('Надо ввести 2 цифры.\n'
                                          'Введи 2 числа через пробел: ')
            elif type_num == '2':
                update.message.reply_text('Надо ввести 4 цифры.\n'
                                          'Введи 4 числа через пробел: ')
            logg.actions_logger('Некорректное значение при вводе чисел')
            return RESULT
    else:
        if type_num == '1':
            update.message.reply_text('Надо вводить цифры.\n'
                                      'Введи 2 числа через пробел: ')
        elif type_num == '2':
            update.message.reply_text('Надо вводить цифры.\n'
                                      'Введи 4 числа через пробел: ')
        logg.actions_logger('Некорректное значение при вводе чисел')
        return RESULT


def menu(update, _):
    global action
    user = update.message.from_user
    logg.entered_logger(user.first_name, update.message.text)
    if action == 'Продолжить':
        update.message.reply_text(f'ОК, посчитаем еще. \n'
                                  f'Выбери с какими числами хочешь работать?\n\n'
                                  '1.Рациональными \n'
                                  '2.Комплексными')
        return ACTION
    elif action == 'Завершить':
        logg.finished_logger(user.first_name, update.message.text)
        update.message.reply_text(
            'Мое дело предложить - Ваше отказаться'
            ' Будет скучно - пиши.')
        return ConversationHandler.END


def cancel(update, _):
    user = update.message.from_user
    logg.finished_logger(user.first_name, update.message.text)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.'
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
            GIVE_NUM: [MessageHandler(Filters.text, give_num)],
            RESULT: [MessageHandler(Filters.text, res)],
            MENU: [MessageHandler(Filters.text, menu)]
        },

        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()
