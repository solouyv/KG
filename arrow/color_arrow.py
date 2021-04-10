#!/usr/bin/env python3

from PIL import Image
import numpy as np
import arrow

import sys
import ipdb


def run_debugger(type, value, tb):
    ipdb.pm()


sys.excepthook = run_debugger


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
                    continue
            else:
                try:
                    if not is_black(pixel) and is_black(row[k + 1]):
                        list_of_lines.append([k, i])
                        in_figure = False
                except IndexError:
                    print(len(list_of_lines), len(list_of_lines) % 2)
                    if len(list_of_lines) % 2 != 0:
                        list_of_lines.pop()
                    continue
    return list_of_lines


def chenge_color(lst, img, color):
    for i, item in enumerate(lst):
        arrow.write_line(lst[0], lst[1], img, color)
        del lst[0:2]


if __name__ == '__main__':
    img = Image.open('arrow.bmp')
    array = np.asarray(img)
    lst = find_lines(array)
    chenge_color(lst, img, (255, 0, 0))
    img.save('arrow.bmp', 'BMP')
