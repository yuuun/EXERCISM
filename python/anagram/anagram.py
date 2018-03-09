def detect_anagrams(word, candidates):
    list_word = list(word.lower())
    res = list()
    for i in range(0, len(candidates)):
        ch = candidates[i]
        list_word.sort()
        list_can = list(ch.lower())
        list_can.sort()
        if list_can == list_word and not word.isupper():
            res.append(candidates[i])
    return res
