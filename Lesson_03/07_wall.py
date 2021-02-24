# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (1200, 600)
side = 0

for shift_y in range(0, 601, 50):
    side -= 50
    for shift_x in range(0, 1801, 100):
        left_corner = sd.get_point(shift_x + side, shift_y,)
        right_corner = sd.get_point(shift_x + side + 100, shift_y + 50,)
        sd.rectangle(left_bottom=left_corner, right_top=right_corner, color=sd.COLOR_RED, width=5)

sd.pause()
