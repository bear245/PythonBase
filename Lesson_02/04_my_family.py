#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['First', 'Second', 'Third']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['First', 100],
    ['Second', 200],
    ['Third', 300]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print("The father's height is " + str(my_family_height[0][1]) + ' cm')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
totalHeight = my_family_height[0][1]+my_family_height[1][1]+my_family_height[1][1]
print("The total height of my family is " + str(totalHeight) + ' cm')
