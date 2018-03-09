def decode(string):
    if string is '': return ''
    switch = 1
    count_digit = ''
    output = ''
    for shr in string:
        if is_digit(shr):
            count_digit += shr
            switch = 0
        elif switch == 1:
            output += shr
        else :
            for i in range(0, int(count_digit)):
                output += shr
            switch = 1
            count_digit = ''
    return output

def encode(string):
    if string is '' : return ''
    output = ''
    count = 1
    for i in range(1, len(string)):
        if string[i] is string[i-1]:
            count += 1
        else :
            output += is_one(count, string[i-1])
            count = 1
    return output + is_one(count, string[i])

def is_one(cnt, shr):
    if cnt is 1 :
        return shr
    else :
        return str(cnt) + shr

def is_digit(shr):
    return '0'<shr<'9'
