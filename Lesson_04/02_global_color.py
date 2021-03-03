# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

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

print("Shape's colors /n "
      "0 = RED, 1 = ORANGE, 2 = YELLOW, 3 = GREEN, "
      "4 = CYAN, 5 = BLUE, 6 = PURPLE")
i = int(input('Select color and press Enter:'))
shape(point=sd.get_point(50, 50), angle=0, length=100, sides=3, color=shape_colors[i])
shape(point=sd.get_point(200, 200), angle=0, length=100, sides=4, color=shape_colors[i])
shape(point=sd.get_point(300, 300), angle=0, length=100, sides=5, color=shape_colors[i])
shape(point=sd.get_point(500, 400), angle=0, length=100, sides=6, color=shape_colors[i])
sd.pause()

