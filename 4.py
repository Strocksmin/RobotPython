import math


def main(n):
    if n == 0:
        return -0.18
    if n == 1:
        return -0.74
    return math.atan(main(n - 2) + main(n - 1) ** 2 + main(n - 1) ** 3) - 1
