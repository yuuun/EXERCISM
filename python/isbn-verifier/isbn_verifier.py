def verify(isbn):
    input_isbn = list(isbn.replace('-', ''))

    if len(input_isbn) is not 10:
        return False
    
    count = 0
    
    for i in range(len(input_isbn)):
        if i <= 9 and is_digit(input_isbn[i]):
            input_isbn[i] = int(input_isbn[i])
            count += input_isbn[i] * (10 - i)
        elif i is 9 and input_isbn[i] is 'X':
            count += 10
        else :
            return False

    if (count%11) is 0:
        return True
    else:
        return False


def is_digit(fig):
    if fig >= '0' and fig <= '9': return True
    else :return False
