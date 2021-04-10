#!/usr/bin/env python3

from PIL import Image


class Fill:
    def __init__(self, img, x, y):
        self.img = img
        self.back_color = img.getpixel((x, y))
        self.stek = [[x, y]]

    def put(self, x, y):
        if self.img.getpixel((x, y)) == self.back_color:
            self.stek.append([x, y])

    def pop(self):
        return self.stek.pop()

    def chenge_color(self, x, y):
        self.img.putpixel((x, y), (0, 0, 255))

    def fill(self):
        while f.stek:
            x, y = f.pop()
            f.chenge_color(x, y)
            f.put(x + 1, y)
            f.put(x, y + 1)
            f.put(x - 1, y)
            f.put(x, y - 1)


if __name__ == '__main__':
    x = 150
    y = 150
    img = Image.open('laba_4.bmp')
    f = Fill(img, x, y)
    f.fill()
    img = f.img
    img.save('laba_6.bmp', 'BMP')
