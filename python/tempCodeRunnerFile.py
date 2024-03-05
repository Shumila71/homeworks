import math


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