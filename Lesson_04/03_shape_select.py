# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

import simple_draw as sd

shape_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
sd.resolution = (1200, 600)

def shape(**kwargs):
    """
    This function draws a shape with several sides and equal length
    :param kwargs:
    point = sd.get_point(200, 200) - start point
    angle(int) = first angle between lines
    length(int) = length of line
    sides(int) = amount of shape's sides with equal length
    :return: None
    """
    point = kwargs.get('point', sd.get_point(200, 200))
    angle = kwargs.get('angle', 0)
    length = kwargs.get('length', 100)
    sides = kwargs.get('sides', 3)
    color = kwargs.get('color', sd.COLOR_RED)
    delta_angle = 360/sides
    v = []
    v.append(sd.get_vector(start_point=point, angle=angle, length=length, width=3))
    v[0].draw(color=color)
    for i in range(sides):
        angle+=delta_angle
        v.append(sd.get_vector(start_point=v[i].end_point, angle=angle, length=length, width=3))
        v[i].draw(color=color)

print("Available shapes: 0 = Triangle, 1 = Square, 2 = Pentagon, 3 = Hexagon")
i = int(input('Select the shape and press Enter:'))
if 0 > i >3:
    print('Incorrect input. Default shape is triangle.')
    i = 0
shape(point=sd.get_point(500, 200), angle=0, length=100, sides=i+3, color=shape_colors[1])
sd.pause()
