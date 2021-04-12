#!/usr/bin/env python3

from PIL import Image
import arrow

lines = [a for a in arrow.lines if a[0][1] != a[1][1]]
# print(lines)

pixels = []
temp = [b for b in map(arrow.find_pixels, lines)]
for a in temp:
    pixels.extend(a)

pixels.sort(key=lambda e: e[1])
# print(pixels)

pixels = [
    a for a in zip(pixels[::2], pixels[1::2]) if a[1][0] - a[0][0] > 1
]
# print(pixels)

pixels = [
    ((a[0] + 1, a[1]), (b[0], b[1])) for a, b in pixels
]
# print(pixels)

print_pixels = []
temp = [b for b in map(arrow.find_pixels, pixels)]
for a in temp:
    print_pixels.extend(a)
# print(pixels)


img = Image.open('arrow.bmp')
arrow.write_line(print_pixels, img, (255, 0, 0))
img.save('green_arrow.bmp', 'BMP')

# for _ in range(top + 1, bottom):


# def find_lines(array):
#     list_of_lines = []
#     in_figure = False
#     for i, row in enumerate(array):
#         for k, pixel in enumerate(row):
#             if not in_figure:
#                 try:
#                     if is_black(pixel) and not is_black(row[k + 1]):
#                         list_of_lines.append([k + 1, i])
#                         in_figure = True
#                 except IndexError:
#                     pass
#             else:
#                 try:
#                     if not is_black(pixel) and is_black(row[k + 1]):
#                         list_of_lines.append([k + 1, i])
#                         in_figure = False
#                 except IndexError:
#                     if len(list_of_lines) % 2 != 0:
#                         list_of_lines.pop()
#                         in_figure = False
#     return list_of_lines


# def chenge_color(lst, img, color):
#     lll = range(len(lst))[::2]
#     for i in lll:
#         arrow.write_line(lst[i], lst[i + 1], img, color)


# if __name__ == '__main__':
#     img = Image.open('arrow.bmp')
#     array = np.asarray(img)
#     lst = find_lines(array)
#     chenge_color(lst, img, (0, 159, 0))
#     img.save('green_arrow.bmp', 'BMP')
