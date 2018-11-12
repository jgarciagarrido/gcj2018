import sys


def solve(area):
    columns = area / 3
    orchard = [[False for i in xrange(0, 1000)] for i in xrange(0, 1000)]
    row = 2
    column = 2
    while column < area-1:
        print "{} {}".format(row, column)
        sys.stdout.flush()
        r, c = [int(s) for s in raw_input().split(" ")]
        if r <= 0 and c <= 0:
            return
        orchard[r-1][c-1] = True
        completed = orchard[row-1][column-1]
        completed = completed and orchard[row-2][column-2]
        completed = completed and orchard[row-1][column-2]
        completed = completed and orchard[row][column-2]
        if completed:
            column += 1
    while r > 0 and c > 0:
        print "{} {}".format(row, column)
        sys.stdout.flush()
        r, c = [int(s) for s in raw_input().split(" ")]


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        area = int(raw_input())
        solve(area)
