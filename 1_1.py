import math


# ИКБО-25-20 Вариант 7

def main(y):
    a = (86 * math.fabs((56 * (y ** 2)) + (95 * y))) + (math.exp(y) ** 7)
    b = (3 + (5 * y ** 3) + (y ** 2)) ** 3
    return (y ** 4 / a) - (b / 18)


print(main(-0.52))
print(main(0.87))
print(main(-0.66))
print(main(-0.51))
print(main(-0.32))
