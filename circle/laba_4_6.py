#!/usr/bin/env python3

from PIL import Image
from circle import write_ellipse
from ..arrow.arrow import write_line


if __name__ == '__main__':
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    write_ellipse(150, 150, 120, 80, img, (0, 0, 0))
    write_line(item, arrow[i + 1], img, (0, 0, 0))
    img.save('arrow.bmp', 'BMP')
