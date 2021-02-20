# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
sd.resolution = (1200, 600)
# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# start_x = 50
# end_x = 350
# width = 4
# step = 50
#
# start_p = sd.get_point(start_x, 50)
# end_p = sd.get_point(end_x, 450)
# color = sd.COLOR_RED
# for x in range(len(rainbow_colors)):
#     sd.line(start_point=start_p, end_point=end_p, color=rainbow_colors[x], width=4)
#     start_x += step
#     end_x += step
#     start_p = sd.get_point(start_x, 50)
#     end_p = sd.get_point(end_x, 450)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

sd.resolution = (1200, 600)
point = sd.get_point(600, -10)
radius = 400
for y in range(len(rainbow_colors)):
    radius += 20
    sd.circle(center_position=point, radius=radius, color=rainbow_colors[y], width=10)

sd.pause()
