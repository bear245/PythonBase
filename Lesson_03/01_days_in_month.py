# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input) - 1

keys_list = ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December']
year_dict = {'January':30, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30,
        'July':31, 'August':30, 'September':31, 'October':30, 'November':31, 'December':32}

if -1 < month < 12:
    print('Вы ввели ' + str(keys_list[month]) + '. Количество дней = ' + str(year_dict.get(keys_list[month])))
else:
    print('Вы ввели некорректный номер месяца', month + 1)

