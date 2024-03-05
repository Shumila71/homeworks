print (42 == 42)
print (42.0 == 42)
print(0b101010 == 42)
print(0o52 == 42)
print(0x2A == 42)
print(int('2A', 16) == 42)
print(ord('*') == 42 )
print(42 + 0j == 42)
print(not not 42 == 42)
print(4.2e+01 == 42)
#1.4
a = 10
while a != 0:
    a -= 0.1#неточность вычислений может не привести ровно к 0
    a = round(a, 1)
print("all ok")
#1.5
z = 1
z <<= 40
# 2 ** z - не хватит памяти
print(z)
#1.6
# i = 0
# while i < 10:
#     print(i)
#здесь 2 операции(бинарный и унарный плюс -> переменная не меняется)    ++i
#1.7
print((True * 2 + False) * -True) #(1*2+0)* -1 = -2
#1.8
x = 5
print(1 < x < 10)#работает как and
print(1 < (x < 10))# (1<True) 1<1 - false

#2.1
#csadasa.()
#2.2
#57=1
#2.3
#print(qrtyu)
#2.4
#a = 'dddddddd
#2.5
#a = "0" + 1
#2.6
# if True:
# print(1)
#2.7
# if True:
#                 print (12)
#         print (1)
#2.8
import math 
# print(math.sqrt(-1))
#2.9
#print(math.exp(10000))

#3.1
i=1
res=0
res= i+i
res = res + res
res = res+res+res
print(res)
#3.2
i=2
res=0 
res= i+i
for b in range(3):
    res += res 
print(res)
#3.3
i=4
res3 = i+i #(*2)
res=(res3<<3) + (res3<<1)#(*20) 
res2=res3+res3
res = res - res2 - i
print("3.3",res)
#3.4
import random

def naive_mul(x, y):
    r = 0
    for i in range(0, y):
        r = x + r
    return r

for i in range(10):
    x = int(random.random())
    y = int(random.random())
    assert naive_mul(x, y) == x + y, "Error"
    print("Test passed")
    
#3.5
print("--------------------------")
def fast_mul(x, y):
    result = 0
    while y:
        if y & 1:  
            result += x
        x <<= 1  
        y >>= 1  
    return result
x = random.randint(0, 10)
y = random.randint(0, 10)
result = fast_mul(x,y)
print(result)
print(x,y)
assert result == (x*y), "nope"
#3.6
# def fast_pow(x, y):
#     result = 1
#     while y:
#         if y & 1: 
#             result *= x
#         x *= x 
#         y >>= 1  
#     return result
# x = random.randint(0, 10)
# y = random.randint(0, 10)
# result = fast_pow(x,y)
# print(result)
# print(x,y)
# assert result == (pow(x,y)), "nope"

#3.7
def mul_bits(x, y, bits=8):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul_16(x, y):
    x_first = (x & 0xFF00) >> 8
    x_second = x & 0xFF
    y_first = (y & 0xFF00) >> 8
    y_second = y & 0xFF
    return (mul_bits(x_first, y_first) << 16) + \
        ((mul_bits(x_first, y_second) + mul_bits(x_second, y_first)) << 8) + \
        mul_bits(x_second, y_second)
x = 0b1100110011001100
y = 0b1010101010101010
print(mul_16(x, y))

#3.8
def mul_bits(x, y, bits=8):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul_16(x, y):
    x_first = (x & 0xFF00) >> 8
    x_second = x & 0xFF
    y_first = (y & 0xFF00) >> 8
    y_second = y & 0xFF
    return (mul_bits(x_first, y_first) << 16) + \
        (mul_bits(x_first, y_second) << 9) + \
        mul_bits(x_second, y_second)
x = 0b1100110011001100
y = 0b1010101010101010
print(mul_16(x, y))
#3.9
import random


def fast_mul_gen(y):
    function_text = f"def f(x):\n"
    function_text += f"    result = 0\n"
    for i in range(y):
        functiontext += f"    result += x\n"
    function_text += f"    return result\n"
    return function_text

def test_fast_mul_gen():
    for i in range(20):
        x = random.randint(1, 20)
        y = random.randint(1, 20)
        local_dict = {}
        exec(fast_mul_gen(y), {}, local_dict)
        f = local_dict['f']
        assert f(x) == x * y

print("All tests passed!")
#3.10
import random
def fast_pow_gen(exp):
    function_text = f"def f(x):\n"
    function_text += f"    result = 1\n"
    for i in range(exp):
        functiontext += f"    result = fast_mul_gen(x)(result)\n"
    function_text += f"    return result\n"
    return function_text

def test_fast_pow_gen():
    for i in range(10):
        x = random.randint(1, 10)
        exp = random.randint(1, 10)
        local_dict = {}
        exec(fast_pow_gen(exp), {}, local_dict)
        f = local_dict['f']
        assert f(x) == x ** exp


print("All tests passed!")
#4.1
# import math
# import tkinter as tk


# def draw(shader, width, height):
#     image = bytearray((0, 0, 0) * width * height)
#     for y in range(height):
#         for x in range(width):
#             pos = (width * y + x) * 3
#             color = shader(x / width, y / height)
#             normalized = [max(min(int(c * 255), 255), 0) for c in color]
#             image[pos:pos + 3] = normalized
#     header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
#     return header + image


# def main(shader):
#     label = tk.Label()
#     img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
#     label.pack()
#     label.config(image=img)
#     tk.mainloop()


# def shader(x, y):
#     if x<0.1 or x>0.9:
#         return 1,1,1
#     elif y<0.1 or y>0.9:
#         return 1,1,1
#     else:
#         return 0,0,0


# main(shader)

#4.2

# import math
# import tkinter as tk


# def draw(shader, width, height):
#     image = bytearray((0, 0, 0) * width * height)
#     for y in range(height):
#         for x in range(width):
#             pos = (width * y + x) * 3
#             color = shader(x / width, y / height)
#             normalized = [max(min(int(c * 255), 255), 0) for c in color]
#             image[pos:pos + 3] = normalized
#     header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
#     return header + image


# def main(shader):
#     label = tk.Label()
#     img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
#     label.pack()
#     label.config(image=img)
#     tk.mainloop()


# def shader(x, y):
#     c1 = createCircle(x, y, 0.53, 0.53, 0.4)
#     c2 = createCircle(x, y, 0.47, 0.47, 0.4)
#     return c2, c1, 0

# def createCircle(x, y, centerX, centerY, radius):
#     distance = math.sqrt((x - centerX) ** 2 + (y - centerY) ** 2)
#     return (radius - distance) * 3


# main(shader)

#4.3
# import math
# import tkinter as tk


# def draw(shader, width, height):
#     image = bytearray((0, 0, 0) * width * height)
#     for y in range(height):
#         for x in range(width):
#             pos = (width * y + x) * 3
#             color = shader(x / width, y / height)
#             normalized = [max(min(int(c * 255), 255), 0) for c in color]
#             image[pos:pos + 3] = normalized
#     header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
#     return header + image


# def main(shader):
#     label = tk.Label()
#     img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
#     label.pack()
#     label.config(image=img)
#     tk.mainloop()


# def shader(x, y):
#     c_x=0.5
#     c_y=0.1
#     r_=0.05
#     center_x = 0.5 
#     center_y = 0.5  
#     radius = 0.4
#     radius_small=0.075
#     distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
#     d_new= math.sqrt((x - c_x) ** 2 + (y - c_y) ** 2)
#     distance_small = math.sqrt((x - 0.65) ** 2 + (y - 0.27) ** 2)
#     if d_new <= r_:
#         return 255,0,255
#     elif (is_inside_triangle(x, y, [(0.45, 0.1), (0.4, 0.15), (0.4, 0.05)]) or \
#                is_inside_triangle(x, y, [(0.55, 0.1), (0.6, 0.15), (0.6, 0.05)])):
#         return 255,0,255
#     elif distance <= radius: 
#         if distance_small <= radius_small:  
#             return 0, 0, 0  
#         else:
#             if (0.6 *x +0.2 < y) or (0.6*x+0.2<-y+1): 
#                 return 255, 255, 0
#             elif (0.57 *x +0.2 < y) or (0.57*x+0.2<-y+1) :
#                 if (x>0.65):
#                     return 255,0,255
#                 else: 
#                     return 255,255,0
#             else:
#                 return 0,0,0
#     else:
#         return 0,0,0 
    
# def is_inside_triangle(x, y, vertices):
#     x1, y1 = vertices[0]
#     x2, y2 = vertices[1]
#     x3, y3 = vertices[2]
#     alpha = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3)) / \
#             ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
#     beta = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3)) / \
#            ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
#     gamma = 1.0 - alpha - beta
#     return 0 <= alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1

# main(shader)

#4.4
# import math
# import tkinter as tk

# def draw(shader, width, height):
#     image = bytearray((0, 0, 0) * width * height)
#     for y in range(height):
#         for x in range(width):
#             pos = (width * y + x) * 3
#             color = shader(x / width, y / height)
#             normalized = [max(min(int(c * 255), 255), 0) for c in color]
#             image[pos:pos + 3] = normalized
#     header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
#     return header + image

# def main(shader):
#     label = tk.Label()
#     img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
#     label.pack()
#     label.config(image=img)
#     tk.mainloop()


# def shader(x, y):
#     return noise(x, y), noise(x, y), noise(x, y)

# def noise(x, y):
#     return (math.sin(x * 127.65424 + y * 2) * 12345.4332) % 1

# main(shader)

#4.5
# import math
# import tkinter as tk


# def draw(shader, width, height):
#     image = bytearray((0, 0, 0) * width * height)
    
#     for y in range(height):
#         for x in range(width):
#             pos = (width * y + x) * 3
#             color = shader(x / width, y / height)
#             normalized = [max(min(int(c * 255), 255), 0) for c in color]
#             image[pos:pos + 3] = normalized
#     header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
#     return header + image


# def main(shader):
#     root = tk.Tk()
#     label = tk.Label(root)
#     img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
#     label.pack()
#     label.config(image=img)
#     root.mainloop()


# def shader(x, y):
#     val = perlinNoise(x, y, 0.05)
#     return val, val, val

# def perlinNoise(x, y, freq):
#     cX = math.floor(x / freq) * freq
#     cY = math.floor(y / freq) * freq
#     freqX = (x - cX) / freq
#     freqY = (y - cY) / freq

#     point1 = noise(cX, cY)
#     point2 = noise(cX + freq, cY)
#     point3 = noise(cX, cY + freq)
#     point4 = noise(cX + freq, cY + freq)

#     return bilerp(point1, point2, point3, point4, increaseNoise(freqX), increaseNoise(freqY))

# def increaseNoise(t):
#     return ((t - 0.5) * 1.4 / (0.2 + abs(t - 0.5)) + 1) * 0.5

# def noise(x, y):
#     return (math.sin(x * 127.65424 + y * 2) * 12345.4332) % 1

# def lerp(a, b, t):
#     return a + (b - a) * t

# def bilerp(point1, point2, point3, point4, tX, tY):
#     return lerp(lerp(point1, point2, tX), lerp(point3, point4, tX), tY)

# main(shader)



#5.1
# import math
# import tkinter as tk


# def draw(shader, width, height):
#     image = bytearray((0, 0, 0) * width * height)
#     for y in range(height):
#         for x in range(width):
#             pos = (width * y + x) * 3
#             color = shader(x / width, y / height)
#             normalized = [max(min(int(c * 255), 255), 0) for c in color]
#             image[pos:pos + 3] = normalized
#     header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
#     return header + image


# def main(shader):
#     label = tk.Label()
#     img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
#     label.pack()
#     label.config(image=img)
#     tk.mainloop()


# def shader(x, y):
#     d = sdf_func(x - 0.5, y - 0.5)
#     return d > 0, abs(d) * 3, 0


# def sdf_func(x, y):
#     return circle(x, y, 0.45)

# def circle(x, y, deg):
#     distance = math.sqrt((x) ** 2 + (y) ** 2)
#     return (deg - distance) * -1


# main(shader)

# #5.2
# import math
# import tkinter as tk


# def draw(shader, width, height):
#     image = bytearray((0, 0, 0) * width * height)
#     for y in range(height):
#         for x in range(width):
#             pos = (width * y + x) * 3
#             color = shader(x / width, y / height)
#             normalized = [max(min(int(c * 255), 255), 0) for c in color]
#             image[pos:pos + 3] = normalized
#     header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
#     return header + image


# def main(shader):
#     label = tk.Label()
#     img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
#     label.pack()
#     label.config(image=img)
#     tk.mainloop()


# def shader(x, y):
#     d = sdf_func(x - 0.5, y - 0.5)
#     return d > 0, abs(d) * 3, 0


# def sdf_func(x, y):
#     return box(x, y, 0.4)

# def box(x, y, deg):
#     distance = max(abs(x), abs(y)) + 0.2
#     return (deg - distance + 0.2) * -1


# main(shader)

#5.3
# import math
# import tkinter as tk


# def draw(shader, width, height):
#     image = bytearray((0, 0, 0) * width * height)
#     for y in range(height):
#         for x in range(width):
#             pos = (width * y + x) * 3
#             color = shader(x / width, y / height)
#             normalized = [max(min(int(c * 255), 255), 0) for c in color]
#             image[pos:pos + 3] = normalized
#     header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
#     return header + image


# def main(shader):
#     label = tk.Label()
#     img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
#     label.pack()
#     label.config(image=img)
#     tk.mainloop()


# def shader(x, y):
#     d = sdf_func(x - 0.5, y - 0.5)
#     return d > 0, abs(d) * 3, 0


# def sdf_func(x, y):
#     return rs(box(x, y, 0.4), circle(x,y,0.3))

# def box(x, y, deg):
#     distance = max(abs(x), abs(y)) + 0.2
#     return (deg - distance + 0.2) * -1

# def circle(x, y, deg):
#     distance = math.sqrt((x) ** 2 + (y) ** 2)
#     return (deg - distance) * -1

# def rs(b,c):
#     return max(b,-c)


# main(shader)

#5.4
# import math
# import tkinter as tk


# def draw(shader, width, height):
#     image = bytearray((0, 0, 0) * width * height)
#     for y in range(height):
#         for x in range(width):
#             pos = (width * y + x) * 3
#             color = shader(x / width, y / height)
#             normalized = [max(min(int(c * 255), 255), 0) for c in color]
#             image[pos:pos + 3] = normalized
#     header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
#     return header + image


# def main(shader):
#     label = tk.Label()
#     img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
#     label.pack()
#     label.config(image=img)
#     tk.mainloop()


# def shader(x, y):
#     d1 = sdf_func1(x - 0.5, y - 0.5)
#     d2 =sdf_func2(x - 0.5, y - 0.5)
#     d3 =sdf_func3(x - 0.5, y - 0.5)
#     d = min(d1,d2,d3)
#     return d > 0, abs(d) * 3, 0


# def sdf_func1(x, y):
#     return circle(x, y, 0.4)
# def sdf_func2(x, y):
#     return circle2(x, y, 0.2)
# def sdf_func3(x, y):
#     return circle3(x, y, 0.2)

# def circle(x, y, deg):
#     distance = math.sqrt((x) ** 2 + (y) ** 2)
#     return (deg - distance) * -1
# def circle2(x, y, deg):
#     distance = math.sqrt((x-0.2) ** 2 + (y+0.3) ** 2)
#     return (deg - distance) * -1
# def circle3(x, y, deg):
#     distance = math.sqrt((x+0.2) ** 2 + (y+0.3) ** 2)
#     return (deg - distance) * -1
# main(shader)

#5.5

# import math
# import tkinter as tk

# WIDTH, HEIGHT = 256, 256


# def draw(shader, width, height):
#     image = bytearray((0, 0, 0) * width * height)
#     for y in range(height):
#         for x in range(width):
#             pos = (width * y + x) * 3
#             color = shader(x/width, y/width)
#             normalized = [max(min(int(c * 255), 255), 0) for c in color]
#             image[pos:pos + 3] = normalized
#             header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
#     return header + image


# def main(shader):
#     label = tk.Label()
#     img = tk.PhotoImage(data=draw(shader, WIDTH, HEIGHT)).zoom(2, 2)
#     label.pack()
#     label.config(image=img)
#     tk.mainloop()


# def box(x, y, deg):
#     distance = max(abs(x+0.2)-0.1, abs(y)-0.4)
#     return distance

# def sdf_func_box(x, y):
#     return box(x, y, 0.3)
# def sdf_func_circle(x,y):
#     return dif(circle(x,y,0.3), circle(x,y,0.1500))

# def circle(x, y, r):
#     d = math.sqrt((x) ** 2 + (y+0.1) ** 2)
#     return (r-d) * -1
# def dif(a,b):
#     return max(a,-b)

# def shader(x, y):
#     d1 = sdf_func_box(x- 0.5, y - 0.5)
#     d2 = sdf_func_circle(x- 0.5, y - 0.5)
#     d = min(d1,d2)
#     return d > 0, abs(d) * 3, 0


# main(shader)


import tkinter as tk
import math

def random(st):
    return math.fmod(math.sin(st[0] * 63.9898 + st[1] * 128.233) * 4788.5453123, 1.0)


def noise(st):
    i = (int(st[0]), int(st[1]))
    f = (st[0] - i[0], st[1] - i[1])
    a = random(i)
    b = random((i[0] + 1, i[1]))
    c = random((i[0], i[1] + 1))
    d = random((i[0] + 1, i[1] + 1))

    u = (f[0] * f[0] * (3.0 - 2.0 * f[0]), f[1] * f[1] * (3.0 - 2.0 * f[1]))

    return a + (b - a) * u[0] + (c - a) * u[1] * (1.0 - u[0]) + (d - b) * u[0] * u[1]


def fbm(st):
    value = 0.0
    amplitude = 0.5

    for _ in range(6):
        value += amplitude * noise(st)
        st = (st[0] * 2, st[1] * 2)
        amplitude *= 0.5

    return value


# Tkinter GUI
class ShaderVisualizer:
    def __init__(self, root, width, height):
        self.root = root
        self.width = width
        self.height = height

        self.canvas = tk.Canvas(root, width=width, height=height,bg="white")
        self.canvas.pack()

        self.draw_shader()

    def draw_shader(self):
        for x in range(self.width):
            for y in range(self.height):
                st = (x / self.width, y / self.height)
                st = (st[0] * self.width / self.height, st[1])

                color = fbm((st[0] * 3.0, st[1] * 3.0))
                color = round(max(0, min(color * 255, 255)))
                blue_shade = 21
                hex_color = "#{:02X}{:02X}{:02X}".format(20, color, 150 )

                self.canvas.create_rectangle(x, y, x + 1, y + 1, fill=hex_color, outline="")

    def run(self):
        self.root.mainloop()
#--------------

# Create and run the visualizer
root = tk.Tk()
root.title("Shader Visualizer")
visualizer = ShaderVisualizer(root, 400, 300)
visualizer.run()
