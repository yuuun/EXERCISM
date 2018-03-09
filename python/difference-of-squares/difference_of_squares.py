def square_of_sum(count):
    tot = 0
    for i in range(1, count+1):
        tot += i
    return tot**2


def sum_of_squares(count):
    tot = 0
    for i in range(1, count+1):
        tot += i**2
    return tot


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
