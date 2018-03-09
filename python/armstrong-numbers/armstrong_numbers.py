def is_armstrong(number):
    cal_sum = 0
    str_number = list(str(number))
    length = len(str_number)
    
    for num in str_number:
        cal_sum += int(num)**length
    return cal_sum == number


