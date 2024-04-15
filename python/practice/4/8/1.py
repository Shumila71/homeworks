from pathlib import Path
import tkinter as tk
from PIL import Image

SCALE_X = 6
SCALE_Y = 4

COLORS = [
    (0, 0, 0),
    (0, 0, 168),
    (0, 168, 0),
    (0, 168, 168),
    (168, 0, 0),
    (168, 0, 168),
    (168, 84, 0),
    (168, 168, 168),
    (84, 84, 84),
    (84, 84, 252),
    (84, 252, 84),
    (84, 252, 252),
    (252, 84, 84),
    (252, 84, 252),
    (252, 252, 84),
    (252, 252, 252)
]


def draw_line(coords, color_index):
    canvas.create_line(*[(x, y) for x, y in coords],
                       fill='#%02x%02x%02x' % COLORS[color_index], width=4)


def draw(pic):
    for i in pic.decode().split("\n"):
        if len(i) == 0:
            continue
        x1, y1, x2, y2, color_index = map(int, i.split())
        draw_line(((x1, y1), (x2, y2)), color_index)


def parse_picture(pic):
    img = Image.open(pic)
    generated = ""
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.getpixel((x, y))
            nearest_value = 1000
            nearest = 0
            for j, i in enumerate(COLORS):
                diff = abs(pixel[0] - i[0]) + abs(pixel[1] - i[1]) + abs(pixel[2] - i[2])
                if diff < nearest_value:
                    nearest = j
                    nearest_value = diff
            generated += f"{x} {y} {x+1} {y+1} {nearest}\n"
    with open("D:\\code\\_4\\python\\practice\\4\\8\\PIC1.txt", "w+") as file:
        file.write(generated)

pic = Path('D:\\code\\_4\\python\\practice\\4\\8\\PIC1.txt').read_bytes()
canvas = tk.Canvas(width=160 * SCALE_X, height=160 * SCALE_Y)
canvas.pack()
draw(pic)
#
tk.mainloop()