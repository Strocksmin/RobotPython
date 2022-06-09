import math


def main(x, y):
    a = (34 * math.log((y ** 3 + 37 * y + 2), 2) ** 7)
    b = (84 * math.exp(x) ** 2)
    c = (math.ceil(x) ** 4) - (math.ceil(92 * y ** 3) ** 2)
    d = 46 * (((y ** 3) / 63) - (x ** 2) - 0.01)
    return ((a + b) / c) + 1 + d


print(main(0.97, 0.28))
print(main(0.48, 0.62))
print(main(0.52, 0.61))
print(main(-0.18, 0.06))
print(main(-0.13, 0.77))