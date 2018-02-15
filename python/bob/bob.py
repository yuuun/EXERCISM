def hey(phrase):
    phrase = phrase.replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '')

    if phrase is '':
        return "Fine. Be that way!"
    
    elif phrase[len(phrase)-1] is '?' and phrase.isupper():
        return "Calm down, I know what I'm doing!"

    elif phrase[len(phrase)-1] is '?':
        return "Sure."

    elif phrase.isupper():
        return "Whoa, chill out!"
    
    else :
        return "Whatever."
