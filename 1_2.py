import math


# ИКБО-25-20 Вариант 10

def main(z, x):
    a = math.sqrt(82 * (math.fabs((z ** 3) + (68 * (x ** 2)) + 1) ** 7))
    b = (70 + x + (18 * (z ** 3))) ** 5
    c = ((math.floor(x) ** 3) / 27) - (z / 60)
    return a + (b / c)


print(main(-0.83, 0.61))
print(main(-0.34, -0.26))
print(main(-0.63, 0.51))
print(main(-0.11, -0.62))
print(main(-0.95, 0.35))
