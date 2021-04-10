#!/usr/bin/env python3

from PIL import Image

img = Image.new('RGB', (800, 800), (255, 255, 255))

start = 399
stop = 400
top = 143
bottom = 654
row = 2
col = 2
b_val = 1
ind = 1
r = 0
g = 255
b = 0

for i in range(800):
    if row == 0:
        row = 2
        g -= 1
        start -= 1
        stop += 1
        b_val = stop - start - ind
        ind += 1
        b = b_val
    if bottom >= i >= top and row != 0:
        row -= 1
    for j in range(800):
        if stop >= j >= start and col == 0 and bottom >= i >= top:
            col = 2
            r += 1
            b -= 1
        if stop >= j >= start and col != 0 and bottom >= i >= top:
            col -= 1
        if bottom >= i >= top:
            if stop >= j >= start:
                if row >= 0:
                    img.putpixel((j, i), (r, g, b))
                    print(r, g, b)
                    if j == stop:
                        r = -1
                        b = b_val

img.save('triangle.bmp', 'BMP')
