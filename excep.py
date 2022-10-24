# import user_interface as us
import logg 

# def mistake(i):
# 	logg.type_num_logger(i)
# 	us.error()
    

def action():
    ls =['+','-','*','/','5']
    while(True):
        i = input('Введите знак: ') 
        if i in ls:
            logg.entered_logger(i)
            return i
        # mistake(i)
        text = "Пользователь ввел: " + i + ". Это некорректный ввод"
        logg.actions_logger(text)


def digit():
    while(True):
        i = input("Введите выбранный пункт: ")
        if i.isdigit():
            logg.entered_logger(i)
            return float(i)
        # mistake(i)
        print("Вам надо ввести число")
        text = "Пользователь ввел: " + i + ". Это некорректный ввод"
        logg.actions_logger(text)

def zero_number(s):
    while(True):
        i = digit_number(s)
        if i !=0 :
            logg.entered_logger(i)
            return i
        # mistake(i)
        print("На ноль делить нельзя")
        text = "Пользователь ввел: 0. Это некорректный ввод"
        logg.actions_logger(text)


def digit_number(s):
    while(True):
        i = input(s)
        k = i.replace('.','')
        k = k.replace('-','')
        if k.isdigit():
            logg.entered_logger(i)
            return float(i)
        # mistake(i)
        print("Вам надо ввести число")
        text = "Пользователь ввел: " + i + ". Это некорректный ввод"
        logg.actions_logger(text)




