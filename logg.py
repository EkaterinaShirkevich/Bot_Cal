from datetime import datetime as dt

def actions_logger(data):
    '''
    Функция, логирует ошибки программы
    :param data: наименование ошибки
    '''
    time = dt.now().strftime('%D %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write(f'{data}, {time} \n')


def entered_logger(data1,data2): # лог ввода от пользователя
    time = dt.now().strftime('%D  %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{}   Сообщение от пользователя {}: {}\n'.format(time,data1, data2))

def type_num_logger(data): # лог выбранных типов чисел
    time = dt.now().strftime('%D  %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{}   Выбранная операция: {}\n'.format(time, data))
        file.write('=' * 60)
        file.write('\n')  

def result_logger(data): # лог результатов операций
    time = dt.now().strftime('%D  %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{}   Результат вычислений: {}\n'.format(time, data))    

def finished_logger(data1,data2): # лог ввода от пользователя
    time = dt.now().strftime('%D  %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{}   Сообщение от пользователя {}: {}\n'.format(time,data1, data2)) 
        file.write('===== Пользователь завершил работу =====\n')  
        file.write('=' * 60)
        file.write('\n')     
