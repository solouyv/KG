#!/usr/bin/env python3

from PIL import Image

lines = (
    ((60, 50), (30, 30)),
    ((30, 30), (140, 30)),
    ((140, 30), (140, 10)),
    ((140, 10), (170, 50)),
    ((170, 50), (140, 90)),
    ((140, 90), (140, 70)),
    ((140, 70), (30, 70)),
    ((30, 70), (60, 50))
)


def find_pixels(line):
    p1 = line[0]
    p2 = line[1]
    pixels = []
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    xerr = yerr = 0

    if dx > 0:
        incX = 1
    elif dx == 0:
        incX = 0
    elif dx < 0:
        incX = -1

    if dy > 0:
        incY = 1
    elif dy == 0:
        incY = 0
    elif dy < 0:
        incY = -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        d = dx
    else:
        d = dy

    x = p1[0]
    y = p1[1]

    pixels.append((x, y))

    for _ in range(d):
        xerr += dx
        yerr += dy

        if xerr > d:
            xerr -= d
            x += incX

        if yerr > d:
            yerr -= d
            y += incY

        pixels.append((x, y))

    return pixels


def write_line(pixels, img, color):
    for pixel in pixels:
        img.putpixel(pixel, color)


if __name__ == '__main__':
    img = Image.new('RGB', (200, 100), (255, 255, 255))

    for line in lines:
        pixels = find_pixels(line)
        write_line(pixels, img, (0, 0, 255))

    img.save('arrow.bmp', 'BMP')
