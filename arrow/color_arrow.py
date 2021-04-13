#!/usr/bin/env python3

from PIL import Image
import arrow

top = min(min(a[0][1], a[1][1]) for a in arrow.lines)
bottom = max(max(a[0][1], a[1][1]) for a in arrow.lines)

d = {tuple(sorted((line[0][1], line[1][1]))):
     arrow.find_pixels(line)
     for line in arrow.lines}

scan_points = []
for i in range(top + 1, bottom):
    lst = set()
    for k in d:
        if k[0] <= i <= k[1]:
            for pixel in d[k]:
                if pixel[1] == i:
                    lst.add(pixel[0])
    scan_points.append((i, sorted(lst)))

print(scan_points)

img = Image.open('arrow.bmp')
for i in scan_points:
    if i[1][-1] - i[1][-2] > 1:
        arrow.write_line(
            arrow.find_pixels(((i[1][-2] + 1, i[0]), (i[1][-1], i[0]))),
            img,
            (255, 0, 0)
        )

img.save('red_arrow.bmp', 'BMP')
