def troubleSortCheck(n, number_list):
    done = False
    while not done:
        done = True
        sorted = True
        first_fail = n
        for i in xrange(0, n-2):
            if number_list[i] > number_list[i+2]:
                done = False
                swap = number_list[i]
                number_list[i] = number_list[i+2]
                number_list[i+2] = swap
            if sorted and i > 0 and number_list[i-1] > number_list[i]:
                first_fail = i-1
                sorted = False
        if sorted and number_list[n-3] > number_list[n-2]:
            first_fail = n-3
            sorted = False
        if sorted and number_list[n-2] > number_list[n-1]:
            first_fail = n-2
            sorted = False
    if sorted:
        return "OK"
    else:
        return first_fail


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n = int(raw_input())
        unsorted_numbers = [int(s) for s in raw_input().split(" ")]
        check = troubleSortCheck(n, unsorted_numbers)
        print "Case #{}: {}".format(i, check)
