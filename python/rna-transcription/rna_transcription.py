def to_rna(dna_strand):
    arr = list(dna_strand)
    b = ''
    for ch in arr:
        if exchange(ch) is 0:
            raise ValueError('Error')
        b += exchange(ch)
    return b


def exchange(x):
    return {'C':'G', 'G':'C', 'T':'A', 'A':'U'}.get(x, 0)
