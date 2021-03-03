# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны

# def triangle(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
#     v3.draw()
#
# triangle(point=point_0, angle=0, length=length_0)

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
    delta_angle = 360/sides
    v = []
    v.append(sd.get_vector(start_point=point, angle=angle, length=length, width=3))
    v[0].draw()
    for i in range(sides):
        angle+=delta_angle
        v.append(sd.get_vector(start_point=v[i].end_point, angle=angle, length=length, width=3))
        v[i].draw()

shape()
shape(point=sd.get_point(50, 50), angle=0, length=100, sides=4)
shape(point=sd.get_point(300, 300), angle=0, length=100, sides=5)
shape(point=sd.get_point(500, 400), angle=0, length=100, sides=6)
sd.pause()
