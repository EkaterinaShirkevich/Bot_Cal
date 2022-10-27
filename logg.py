from datetime import datetime as dt

def actions_logger(data):
    '''
    Функция, логирует ошибки программы
    :param data: наименование ошибки
    '''
    time = dt.now().strftime('%D  %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write(f'{time}   {data} \n')


def entered_logger(data1,data2): # лог ввода от пользователя
    time = dt.now().strftime('%D  %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{}   Сообщение от пользователя {}: {}\n'.format(time,data1, data2))


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
