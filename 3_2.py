import math


def main(m, n, a):
    total = 0
    prod = 1
    total2 = 0
    for k in range(1, a + 1):
        for j in range(1, n + 1):
            for c in range(1, m + 1):
                total += (k ** 18) + (math.sqrt(j ** 3 + ((c ** 2) / 2))) ** 7
            prod *= total
            total = 0
        total2 += prod
        prod = 1
    return total2


print(main(5, 2, 7))
print(main(6, 3, 5))
print(main(7, 3, 8))
print(main(8, 2, 6))
print(main(7, 2, 4))
