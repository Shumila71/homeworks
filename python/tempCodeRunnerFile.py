import math
def calculate_expression(j, k, c, y):
    return 42*c**5-20*(1+j**2+81*k**3)-math.exp(y)**7

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
