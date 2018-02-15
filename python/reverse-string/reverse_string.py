def reverse(input=''):
    a = list(input)
    a.reverse()
    b = ''
    
    for ch in a:
        b += ch
    return b
