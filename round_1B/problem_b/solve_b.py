#!/usr/bin/env python
# -*- coding: utf-8 -*-


def valid_set(signs):
    extended = extend_signs(signs)
    sign = extended[0]
    m = sign[3]
    n = sign[4]
    size = 1
    for sign in extended[1:]:
        if (m == sign[3]) or (n == sign[4]):
            size += 1
        else:
            return size
    return size


def extend_signs(signs):
    return [(x[0], x[1], x[2], x[0] + x[1], x[0] - x[2]) for x in signs]


def max_set_and_number_of_sets(signs, number_of_signs):
    max_size = 0
    number_of_sets = 0
    for i in xrange(number_of_signs):
        subset = signs[i:]
        size = valid_set(subset)
        if (size == max_size):
            number_of_sets += 1
        elif (size > max_size):
            max_size = size
            number_of_sets = 1
        if (i+max_size >= number_of_signs):
            return (max_size, number_of_sets)


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n = int(raw_input())
        signs = []
        for j in xrange(n):
            sign = [int(s) for s in raw_input().split(" ")]
            signs.append(sign)
        max_size, number_of_sets = max_set_and_number_of_sets(signs, n)
        print "Case #{}: {} {}".format(i, max_size, number_of_sets)
