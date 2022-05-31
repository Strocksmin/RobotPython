import math


def main(x):
    n = len(x)
    x.insert(0, 0)
    total = 0
    for i in range(1, n + 1):
        total += ((x[math.ceil(i/3)] ** 2) + (x[math.ceil(i/3)] ** 3)) ** 4
    return total
