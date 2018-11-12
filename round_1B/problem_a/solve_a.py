#!/usr/bin/env python
# -*- coding: utf-8 -*-


def percents(favorites, n):
    return [100.0 * fav/n for fav in favorites]


def max_sum(n, langs, favorites):
    persons_answer = sum(favorites)
    persons_not_answer = (n - persons_answer)
    perc_answer = percents(favorites, n)
    perc_not_answer = 100.0 * persons_not_answer / n
    round_answer = [int(round(x)) for x in perc_answer]
    round_not_answer = int(round(perc_not_answer))
    sum_answer = sum(round_answer)
    max_sum = sum_answer + round_not_answer

    perc_not_answer = 100.0 / n
    round_not_answer = int(round(perc_not_answer))
    variant_sum = sum_answer + (persons_not_answer * round_not_answer)
    max_sum = max(max_sum, variant_sum)
    for i in xrange(len(favorites)):
        variant = list(perc_answer)
        variant[i] += perc_not_answer
        round_variant = [int(round(x)) for x in variant]

        variant_sum = sum(round_variant)
        max_sum = max(max_sum, variant_sum)

    return max_sum


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, langs = [int(s) for s in raw_input().split(" ")]
        favorites = [int(s) for s in raw_input().split(" ")]
        print "Case #{}: {}".format(i, max_sum(n, langs, favorites))
