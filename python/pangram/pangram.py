def is_pangram(sentence):
    a = list(sentence.lower())
    b = [0]*26
    for ch in a :
        num = ord(ch) - ord('a')
        if num >= 0 and num < 26:
            b[num] = b[num] +1
    for i in b:
        if i is 0 : return False
        
    return True
        
