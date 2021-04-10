#!/usr/bin/env python3

from PIL import Image

arrow = (
    (60, 50), (30, 30), (140, 30), (140, 10), (170, 50),
    (140, 90), (140, 70), (30, 70), (60, 50)
)


def write_line(p1, p2, img, color):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    xerr = yerr = 0

    if dx > 0: incX = 1
    elif dx == 0: incX = 0
    elif dx < 0: incX = -1

    if dy > 0: incY = 1
    elif dy == 0: incY = 0
    elif dy < 0: incY = -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy: d = dx
    else: d = dy

    x = p1[0]
    y = p1[1]
    img.putpixel((x, y), color)
    for _ in range(d):
        xerr += dx
        yerr += dy

        if xerr > d:
            xerr -= d
            x += incX

        if yerr > d:
            yerr -= d
            y += incY
        img.putpixel((x, y), color)


if __name__ == '__main__':
    img = Image.new('RGB', (200, 100), (255, 255, 255))

    for i, item in enumerate(arrow[:-1]):
        write_line(item, arrow[i + 1], img, (0, 0, 0))

    img.save('arrow.bmp', 'BMP')
