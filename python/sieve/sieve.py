import math
def sieve(limit):
    res = list()
    if limit > 1:
        for x in range(2, limit+1):
            fig = True
            for j in range(2, int(x/2)+1):
                if x % j == 0:
                    fig = False
                    break;
            if fig:
                res.append(x)
    return res
