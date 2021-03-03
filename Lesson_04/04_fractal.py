# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (600, 800)
point_0 = sd.get_point(300, 5)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции


def branch(point, angle, length, delta=30):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=point, angle=angle-30, length=length, width=3)
    v2.draw()
    next_point_v1 = v1.end_point
    next_angle_v1 = angle + delta * (sd.random_number(0, 40)/100)
    next_length_v1 = length * .75
    next_point_v2 = v2.end_point
    next_angle_v2 = angle - delta * (sd.random_number(0, 40)/100)
    next_length_v2 = length * .75
    branch(point=next_point_v1, angle=next_angle_v1, length=next_length_v1, delta=delta)
    branch(point=next_point_v2, angle=next_angle_v2, length=next_length_v2, delta=delta)

branch(point=point_0, angle=105, length=150, delta=30)

# for delta in range(0, 51, 10):
#     branch(point=point_0, angle=90, length=150, delta=delta)
# for delta in range(-50, 1, 10):
#     branch(point=point_0, angle=90, length=150, delta=delta)


sd.pause()

sd.pause()


