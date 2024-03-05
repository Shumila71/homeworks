def calculate_expression(j, k, c, y):
    return (34 * j ** 2) ** 3 + (y / 9 + 86 * k ** 3) ** 2 + 94 * c ** 5

def recursive_sum(m, a, b, y, j=1, k=1, c=1):
    if c > b:
        return 0
    if k > a:
        return recursive_sum(m, a, b, y, j, 1, c + 1)
    if j > m:
        return recursive_sum(m, a, b, y, 1, k + 1, c)
    return calculate_expression(j, k, c, y) + recursive_sum(m, a, b, y, j + 1, k, c)

def main(m, a, b, y):
    return recursive_sum(m, a, b, y)

# Примеры вызова функции
print(main(2, 4, 4, 0.96))  # Результат должен соответствовать обновленному выражению
print(main(3, 2, 4, -0.06)) # Результат должен соответствовать обновленному выражению
print(main(3, 3, 6, -0.68)) # Результат должен соответствовать обновленному выражению
print(main(2, 6, 8, -0.77)) # Результат должен соответствовать обновленному выражению
print(main(3, 7, 4, 0.85))  # Результат должен соответствовать обновленному выражению