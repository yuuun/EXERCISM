def is_isogram(string):
    if string == "": return True
    a = list(string.lower())
    b = [a[0]]
    for i in range(1, len(string)):
        if  a[i] in b and a[i] is not ' ' and a[i] is not '-':
                return False
        b.append(a[i])
    return True
