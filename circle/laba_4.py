#!/usr/bin/env python3

import math
from PIL import Image


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


def write_ellipse(xc, yc, enx, eny, img, color):
    a = int(abs(enx - xc))
    b = int(abs(eny - yc))
    a2 = a ** 2
    b2 = b ** 2
    dds = 4 * a2
    ddt = 4 * b2
    dxt = int(a2 / math.sqrt(a2 + b2))
    t = 0
    s = -4 * a2 * b
    e = (-s / 2) - 2 * b2 - a2
    ca = -6 * b2
    cd = ca - 4 * a2
    x = xc
    y = yc + b

    img.putpixel((x, y), color)
    img.putpixel((x, 2 * yc - y), color)
    img.putpixel((2 * xc - x, 2 * yc - y), color)
    img.putpixel((2 * xc - x, y), color)

    for _ in range(dxt):
        x += 1
        if (e >= 0):
            e += (t + ca)
        else:
            y -= 1
            e += (t - s + cd)
            s += dds
        t -= ddt
        img.putpixel((x, y), color)
        img.putpixel((x, 2 * yc - y), color)

    dxt = abs(y - yc)
    e -= (t / 2 + s / 2 + b2 + a2)
    ca = -6 * a2
    cd = ca - 4 * b2

    for _ in range(dxt):
        y -= 1
        if (e <= 0):
            e += (-s + ca)
        else:
            x += 1
            e += (-s + t + cd)
            t -= ddt
        s += dds
        img.putpixel((x, y), color)
        img.putpixel((x, 2 * yc - y), color)


if __name__ == '__main__':
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    lines = (
        ((65, 150), (90, 90)),
        ((90, 90), (200, 90)),
        ((200, 210), (90, 210)),
        ((90, 210), (65, 150))
    )
    for item1, item2 in lines:
        write_line(item1, item2, img, (0, 0, 0))

    write_ellipse(200, 150, 170, 210, img, (0, 0, 0))

    img.save('laba_4.bmp', 'BMP')
