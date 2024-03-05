import math


def func1(z):
    return ((81 - z / 69 - 81 * z ** 3) ** 2 - (abs(z)) ** 6)


def func2(z):
    return 45 * (1 - 39 * z) ** 6


def func3(z):
    return z ** 3


def func4(z):
    return math.cos(z) ** 5


def main(z):
    functions = {z < -30: func1, -30 <= z < -15: func2,
                 -15 <= z < 84: func3, 84 <= z: func4}
    result = functions[True](z)
    return result



print(main(66))  # Ожидаемый результат: 2.87e+05
print(main(-10))  # Ожидаемый результат: -1.00e+03
print(main(104))  # Ожидаемый результат: -7.61e-01
print(main(72))  # Ожидаемый результат: 3.73e+05
print(main(-17))  # Ожидаемый результат: 3.86e+18

