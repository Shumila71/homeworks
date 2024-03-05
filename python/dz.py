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