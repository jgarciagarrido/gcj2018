from math import sqrt


def rotate_z(p, cos_alpha):
    sin_alpha = sqrt(1 - cos_alpha * cos_alpha)
    x = p[0] * cos_alpha - p[1] * sin_alpha
    y = p[0] * sin_alpha + p[1] * cos_alpha
    return [x, y, p[2]]


def rotate_x(p, cos_alpha):
    sin_alpha = sqrt(1 - cos_alpha * cos_alpha)
    y = p[1] * cos_alpha - p[2] * sin_alpha
    z = p[1] * sin_alpha + p[2] * cos_alpha
    return [p[0], y, z]


def max_rotation(area):
    points = [
        [0.3535533905932738, 0.3535533905932738, 0.0],
        [-0.3535533905932738, 0.3535533905932738, 0.0],
        [0.0, 0.0, 0.5]
    ]
    if area <= 1.414213:
        cos_alpha = area / 1.414213
        rotate = rotate_z
    else:
        cos_alpha = area / 2.414213
        rotate = rotate_x

    return map(lambda point: rotate(point, cos_alpha), points)


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        area = float(raw_input())  # read a list of integers, 2 in this case
        points = max_rotation(area)
        print "Case #{}:".format(i)
        for point in points:
            print "{0[0]:.8f} {0[1]:.8f} {0[2]:.8f}".format(point)
