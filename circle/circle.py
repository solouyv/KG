#!/usr/bin/env python3

from PIL import Image
import math


def write_circle(xc, yc, radius, img, color):
    r2 = radius ** 2
    dst = 4 * r2
    dxt = int(radius / math.sqrt(2)) + 1
    t = 0
    s = -4 * r2 * radius
    e = (-s / 2) - 3 * r2
    ca = - 6 * r2
    cd = -10 * r2
    x = 0
    y = radius

    img.putpixel((xc, yc + radius), color)
    img.putpixel((xc, yc - radius), color)
    img.putpixel((xc + radius, yc), color)
    img.putpixel((xc - radius, yc), color)

    for _ in range(dxt):
        x += 1
        if e >= 0:
            e += (t + ca)
        else:
            y -= 1
            e += (t - s + cd)
            s += dst

        t -= dst

        img.putpixel((xc + x, yc + y), color)
        img.putpixel((xc + y, yc + x), color)
        img.putpixel((xc + y, yc - x), color)
        img.putpixel((xc + x, yc - y), color)
        img.putpixel((xc - x, yc - y), color)
        img.putpixel((xc - y, yc - x), color)
        img.putpixel((xc - y, yc + x), color)
        img.putpixel((xc - x, yc + y), color)


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
        img.putpixel((2 * xc - x, 2 * yc - y), color)
        img.putpixel((2 * xc - x, y), color)

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
        img.putpixel((2 * xc - x, 2 * yc - y), color)
        img.putpixel((2 * xc - x, y), color)


if __name__ == '__main__':
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    write_circle(150, 150, 120, img, (0, 0, 0))
    write_circle(150, 150, 118, img, (0, 0, 0))
    write_circle(150, 150, 116, img, (0, 0, 0))
    write_circle(150, 150, 114, img, (0, 0, 0))
    write_circle(150, 150, 112, img, (0, 0, 0))
    write_circle(150, 150, 110, img, (0, 0, 0))
    write_circle(150, 150, 108, img, (0, 0, 0))
    write_circle(150, 150, 106, img, (0, 0, 0))
    img.save('circle.bmp', 'BMP')
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    write_ellipse(150, 150, 120, 80, img, (0, 0, 0))
    write_ellipse(150, 150, 118, 78, img, (0, 0, 0))
    write_ellipse(150, 150, 116, 76, img, (0, 0, 0))
    write_ellipse(150, 150, 114, 74, img, (0, 0, 0))
    write_ellipse(150, 150, 112, 72, img, (0, 0, 0))
    write_ellipse(150, 150, 110, 70, img, (0, 0, 0))
    write_ellipse(150, 150, 108, 68, img, (0, 0, 0))
    write_ellipse(150, 150, 106, 66, img, (0, 0, 0))
    img.save('ellipse.bmp', 'BMP')
