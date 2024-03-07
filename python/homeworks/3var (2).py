def calculate_expression(j, k, c, y):
    return ((34 * j ** 2) ** 3
            + (y / 9 + 86*k ** 3) ** 2 + 94*c**5)

def main(m, a, b, y):
    return sum(calculate_expression(j, k, c, y) for
               c in range(1, b + 1) for k in range(1, a + 1) for j in range(1, m + 1))

# Примеры вызова функции
print(main(2, 4, 4, 0.96))  # должно быть приблизительно 3.31e+08
print(main(3, 2, 4, -0.06)) # должно быть приблизительно 2.56e+08
print(main(3, 3, 6, -0.68)) # должно быть приблизительно 6.78e+08
print(main(2, 6, 8, -0.77)) # должно быть приблизительно 8.14e+09
print(main(3, 7, 4, 0.85))  # должно быть приблизительно 1.73e+10