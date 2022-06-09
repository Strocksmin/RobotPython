import math


def main(n, b):
    prod = 1
    total = 0
    for i in range(1, b + 1):
        for k in range(1, n + 1):
            total += (i ** 3) - (k ** 4)
        prod *= total
        total = 0
    total2 = 0
    for i in range(1, b + 1):
        total2 += ((i ** 5) - (13 * i ** 3) - 59)
    return prod + total2


print(main(4, 8))
print(main(6, 4))
print(main(4, 3))
print(main(7, 4))
print(main(4, 5))
print(main(1, 1))