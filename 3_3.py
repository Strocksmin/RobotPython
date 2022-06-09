import math


def main(n, p, b):
    total = 0
    for c in range(1, n + 1):
        total += 70 * c ** 3 - 30 * (c - c ** 3 / 89) ** 4 - ((math.floor(p)) ** 5) / 27
    prod = 1
    for c in range(1, b + 1):
        prod *= c ** 4
    return total + prod


print(main(5, -0.59, 3))
print(main(2, -0.27, 3))
print(main(7, 0.5, 8))
print(main(4, -0.07, 3))
print(main(7, 0.81, 3))
