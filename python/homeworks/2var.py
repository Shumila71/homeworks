import math


def calculate_first_case(z):
    return ((81 - z / 69 - 81 * z ** 3) ** 2 - (abs(z)) ** 6)


def calculate_second_case(z):
    return 45 * (1 - 39 * z) ** 6


def calculate_third_case(z):
    return z ** 3


def calculate_fourth_case(z):
    return math.cos(z) ** 5


cases = [
    (lambda z: z < -30, calculate_first_case),
    (lambda z: -30 <= z < -15, calculate_second_case),
    (lambda z: -15 <= z < 84, calculate_third_case),
    (lambda z: z >= 84, calculate_fourth_case),
]


def main(z):
    return next(func(z) for condition, func in cases if condition(z))


print(main(66))  # Ожидаемый результат: 2.87e+05
print(main(-10))  # Ожидаемый результат: -1.00e+03
print(main(104))  # Ожидаемый результат: -7.61e-01
print(main(72))  # Ожидаемый результат: 3.73e+05
print(main(-17))  # Ожидаемый результат: 3.86e+18

