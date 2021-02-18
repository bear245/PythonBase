# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)

# keys_list = ['January', 'February', 'March', 'April', 'May', 'June',
#         'July', 'August', 'September', 'October', 'November', 'December']
# year_dict = {'January':30, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30,
#         'July':31, 'August':30, 'September':31, 'October':30, 'November':31, 'December':32}
#
# if -1 < month < 12:
#     print('Вы ввели ' + str(keys_list[month]) + '. Количество дней = ' + str(year_dict.get(keys_list[month])))
# else:
#     print('Вы ввели некорректный номер месяца', month + 1)

if not (1 <= month <= 12):
    print('Вы ввели некорректный номер месяца', month)
elif month == 1:
    print('30 days')
elif month == 2:
    print('28 days')
elif month == 3:
    print('31 days')
elif month == 4:
    print('30 days')
elif month == 5:
    print('31 days')
elif month == 6:
    print('30 days')
elif month == 7:
    print('31 days')
elif month == 8:
    print('30 days')
elif month == 9:
    print('31 days')
elif month == 10:
    print('30 days')
elif month == 11:
    print('30 days')
elif month == 12:
    print('31 days')
