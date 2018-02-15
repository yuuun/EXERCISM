def distance(strand_a, strand_b):
    cmp_a = list(strand_a)
    cmp_b = list(strand_b)
    count = 0

    if len(strand_a) is not len(strand_b):
        raise ValueError('Error')
    
    for i in range(len(strand_a)):
        if cmp_a[i] is not cmp_b[i]:
            count += 1
            
    return count
