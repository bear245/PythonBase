# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37
copy_a = a
count = 0

while a > b:
    a -= b
    count += 1

print('Целочисленное деление ' + str(copy_a) + ' на ' + str(b) + ' дает ' + str(count))
