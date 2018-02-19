import re
def word_count(phrase):
    dic_a = {}
    phrase = phrase.replace('_', " ")
    phrase_a = re.findall(r"[\w']+", phrase.lower())

    for word in phrase_a:
        if word[0] is "'":
            word = word.replace("'", "")
        if word not in dic_a:
            dic_a[word] = 1
        else :
            dic_a[word] += 1

    return dic_a
