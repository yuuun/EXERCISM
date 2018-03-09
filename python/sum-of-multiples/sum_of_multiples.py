def sum_of_multiples(limit, multiples):
    sum_mul = set()
    for i in multiples:
        j = 1
        while((i*j)<limit):
            sum_mul.add((i*j))
            j += 1
    return sum(sum_mul)
