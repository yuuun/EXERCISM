def rotate(text, key):
    ret_text = ''
    for ch in text:
        ord_ch = chr(ord(ch)+key)
        if isalpha(ch):
            if isalpha(ord_ch) and not (isdown(ord_ch) and isup(ch)):
                ret_text += ord_ch
            else :
                ret_text += chr(ord(ch) + key -26)
        else :
            ret_text += ch
    return ret_text

def isdown(ch):
    return 'a'<= ch <= 'z'

def isup(ch):
    return 'A'<= ch <= 'Z'

def isalpha(ch):
    return isdown(ch) or isup(ch)
