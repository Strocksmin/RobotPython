import math


def main(m, a, x):
    total1 = 0
    total2 = 0
    for i in range(1, m + 1):
        total1 += 0.02 + (3 * (math.exp((i ** 2) - (i ** 3)) ** 4))
    for j in range(1, m + 1):
        for k in range(1, a + 1):
            total2 += (28 * k) + 81 + (22 * ((1 - 52 * x ** 2 - 50 * j) ** 7))
    return total1 - total2
