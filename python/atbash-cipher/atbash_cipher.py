def encode(plain_text):
    res = ''
    plain_text = plain_text.replace(" ", "").replace(",", "").replace(".", "").lower()
    for i in range(0, len(plain_text)):
        ch = plain_text[i]
        if i % 5  == 0 and i != 0:
            res += " "
        res += change_alpha(ch)
    return res
    
def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(" ", "")
    res = ""
    for i in range(0, len(ciphered_text)):
        ch = ciphered_text[i]
        res += change_alpha(ch)
    return res

def change_alpha(ch):
    if ch.isalpha():
        return chr(219 - ord(ch))
    else :
        return ch
        
