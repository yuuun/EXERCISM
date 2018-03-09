def slices(series, length):
    res = list()
    if len(series) < length or length == 0:
        raise ValueError("ValueError not raised")
    for i in range(0, len(series)- length+1):
        append_list = list(series[i])
        for x in range(1, length):
            append_list.append(series[i+x])
        append_list = [int (j)for j in append_list]
        res.append(append_list)
    return res
