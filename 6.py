def zero(items, left, middle, right):
    if items[0] == 1997:
        return left
    if items[0] == 2018:
        return middle
    if items[0] == 1972:
        return right


def four(items, left, middle, right):
    if items[4] == 'STATA':
        return left
    if items[4] == 'SCALA':
        return middle
    if items[4] == 'XSLT':
        return right


def three(items, left, middle):
    if items[3] == 1979:
        return left
    if items[3] == 1964:
        return middle


def two(items, left, middle, right):
    if items[2] == 1989:
        return left
    if items[2] == 1983:
        return middle
    if items[2] == 2016:
        return right


def one(items, left, right):
    if items[1] == 1967:
        return left
    if items[1] == 1986:
        return right


def main(items):
    return four(items,
                one(items,
                    three(items,
                          two(items, 0, 1, 2),
                          3),
                    two(items, 4, 5,
                        zero(items, 6, 7, 8))),
                9,
                10)
