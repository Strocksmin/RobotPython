import math


def main(x):
    if x < 83:
        return 26 * (math.fabs(91 * x ** 2) ** 5) - 2 - (31 * math.floor(x))
    if 83 <= x < 162:
        return 79 * (math.exp((x ** 2 / 31) - (x ** 3) - 1) ** 5)
    if 162 <= x < 246:
        return ((38 * x ** 2 + (x / 22) + 1) ** 7) - \
               ((x ** 3 - x ** 2 - 1) ** 5)
    if 246 <= x < 326:
        return math.atan(x) ** 2 - (x ** 4) - 11
    if x >= 326:
        return 33 * math.tan(45 + x ** 3) ** 6 - (25 * x ** 7)
