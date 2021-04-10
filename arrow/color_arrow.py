#!/usr/bin/env python3

from PIL import Image
import numpy as np
import arrow


def is_black(pixel):
    if 0 in pixel:
        return True


def find_lines(array):
    list_of_lines = []
    in_figure = False
    for i, row in enumerate(array):
        for k, pixel in enumerate(row):
            if not in_figure:
                try:
                    if is_black(pixel) and not is_black(row[k + 1]):
                        # import debug
                        list_of_lines.append([k + 1, i])
                        in_figure = True
                except IndexError:
                    pass
            else:
                try:
                    if not is_black(pixel) and is_black(row[k + 1]):
                        list_of_lines.append([k + 1, i])
                        in_figure = False
                except IndexError:
                    if len(list_of_lines) % 2 != 0:
                        list_of_lines.pop()
                        in_figure = False
    return list_of_lines


def chenge_color(lst, img, color):
    lll = range(len(lst))[::2]
    for i in lll:
        arrow.write_line(lst[i], lst[i + 1], img, color)


if __name__ == '__main__':
    img = Image.open('arrow.bmp')
    array = np.asarray(img)
    lst = find_lines(array)
    chenge_color(lst, img, (0, 159, 0))
    img.save('green_arrow.bmp', 'BMP')
