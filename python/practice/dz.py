# from math import * 
# def main(z,x):
#     result = 43*(16*x-56*z**2-1)**4/(z**7-((acos(x**2))**3)/80) - sqrt(((x**3)/54+(cos(x+z**2+86))**2)/(96*((sqrt(28*z**3)))**4-log(x**2+0.07)**7 ))
#     return result



# import math


# def main(z, x):
#     return 43 * (16 * x - 56 * z**2 - 1) ** 4 / (
#         z**7 - ((math.acos(x**2)) ** 3) / 80
#     ) - math.sqrt(
#         ((x**3) / 54 + (math.cos(x + z**2 + 86)) ** 2)
#         / (96 * ((math.sqrt(28 * z**3))) ** 4 - math.log(x**2 + 0.07) ** 7)
#     )

# import math


# def calculate_first_case(z):
#     return 47*z**3+90*z**2+(z**2-65*z**3)**5


# def calculate_second_case(z):
#     return 59*(63*z**3)**4-abs(z**3)-z**5


# def calculate_fourth_case(z):
#     return (44-z)**3-41*math.log(64*z**2-55)**4-z**7


# cases = [
#     (lambda z: z < 93, calculate_first_case),
#     (lambda z: 93 <= z < 183, calculate_second_case),
#     (lambda z: z >= 183, calculate_fourth_case),
# ]


# def main(z):
#     return next(func(z) for condition, func in cases if condition(z))


# print(main(51))  # Ожидаемый результат: -4.76e+34



# def func1(z):
#     return 47*z**3+90*z**2+(z**2-65*z**3)**5


# def func2(z):
#     return 59*(63*z**3)**4-abs(z**3)-z**5



# def func4(z):
#     return (44-z)**3-41*math.log(64*z**2-55)**4-z**7


# def main(z):
#     functions = {z < 93: func1, 93 <= z < 183: func2, 183 <= z: func4}
#     result = functions[True](z)
#     return result
# import math
# def main(m, a, b, y):
#     total_sum = 0
#     for c in range(1, b + 1):
#         for k in range(1, a + 1):
#             for j in range(1, m + 1):
#                 total_sum += (42*c**5-20*(1+j**2+81*k**3)-math.exp(y)**7)
#     return total_sum

# def calculate_expression(j, k, c, y):
#     return 42*c**5-20*(1+j**2+81*k**3)-math.exp(y)**7

# def recursive_sum(m, a, b, y, j=1, k=1, c=1):
#     if c > b:
#         return 0
#     if k > a:
#         return recursive_sum(m, a, b, y, j, 1, c + 1)
#     if j > m:
#         return recursive_sum(m, a, b, y, 1, k + 1, c)
#     return calculate_expression(
#         j, k, c, y) + recursive_sum(m, a, b, y, j + 1, k, c)

# def main(m, a, b, y):
#     return recursive_sum(m, a, b, y)

# from functools import reduce

# def calculate_expression(j, k, c, y):
#     return 42*c**5-20*(1+j**2+81*k**3)-math.exp(y)**7

# def main(m, a, b, y):
#     return reduce(
#         lambda acc, c: acc + reduce(
#             lambda acc_k, k: acc_k + reduce(
#                 lambda acc_j, j: acc_j + calculate_expression(j, k, c, y),
#                 range(1, m + 1),
#                 0
#             ),
#             range(1, a + 1),
#             0
#         ),
#         range(1, b + 1),
#         0
#     )
import math
def calculate_expression(j, k, c, y):
    return 42*c**5-20*(1+j**2+81*k**3)-math.exp(y)**7

def main(m, a, b, y):
    return sum(calculate_expression(j, k, c, y) for
               c in range(1, b + 1) for k in range(1, a + 1) for j in range(1, m + 1))
print(main(2, 3, 7, -0.52))  # должно быть приблизительно 6.49e+06
# import math


# def main(n):
#     return (
#         -0.97
#         if n == 0
#         else 0.9
#         if n == 1
#         else (pow((
#             math.ceil(main(n - 2))), 3)) - (
#                 pow((main(n - 2)), 3) + pow((
#                     main(n - 2)), 2) + main(n - 1) ) - 2
#         )
import math
def main(n):
    match n:
        case 0:
            return -0.97
        case 1:
            return 0.9
        case _ if n >= 2:
            return (pow((
            math.ceil(main(n - 2))), 3)) - (
                pow((main(n - 2)), 3) + pow((
                    main(n - 2)), 2) + main(n - 1) ) - 2
# import math

# def main(n):
#     return (
#         -0.97
#         if n == 0
#         else 0.9
#         if n == 1
#         else math.ceil(main(n - 2)) ** 3 - (main(n - 2) ** 3 + main(n - 2) ** 2 + main(n - 1)) - 2
#         else math.ceil(main(n - 2) ** 3) - (main(n - 2) ** 3 + main(n - 2) ** 2 + main(n - 1)) - 2
#     )

print(main(7))

