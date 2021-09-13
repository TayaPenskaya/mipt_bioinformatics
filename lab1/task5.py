def hamming_distance(str1, str2):
    dist = 0
    for i in range(len(str1)):
        if (str1[i] != str2[i]):
            dist += 1
    return dist

def neighbors(pattern, d):
    symb = {'A', 'G', 'C', 'T'}
    if (d == 0):
        return {pattern}
    if (len(pattern) == 1):
        return symb
    ns = []
    sufset = neighbors(pattern[1:], d)
    for suf in sufset:
        if (hamming_distance(pattern[1:], suf) < d):
            for s in symb:
                ns.append(s + suf)
        else:
            ns.append(pattern[0] + suf)

    return set(ns)

def complement_reverse(text):
    complements = {
        'A': 'T',
        'G': 'C',
        'T': 'A',
        'C': 'G'
    }
    res = ''
    for l in text:
        res += complements[l]
    return res[::-1]

def freq_words_with_mismatch_and_reverse(text, k, d):
    wmap = {}
    res = []

    for i in range(len(text)-k):
        pattern = text[i:i+k]
        comp = complement_reverse(pattern)
        ns = neighbors(pattern, d)
        cns = neighbors(comp, d)
        all_ns = list(ns) + list(cns)
        for n in all_ns:
            cn = complement_reverse(n)
            npair = [n, cn]
            for n_ in npair:
                if (n_ not in wmap):
                    wmap[n_] = 1
                else:
                    wmap[n_] += 1

    vmax = 0
    for k, v in wmap.items():
        vcur = v + wmap[complement_reverse(k)]
        if (vcur == vmax):
            res.append(k)
        elif (vcur > vmax):
            vmax = vcur
            res = [k]

    return ' '.join(res)

with open('rosalind_ba1j.txt') as f:
    text = f.readline()[:-1]
    k, d = list(map(int, f.readline()[:-1].split()))
    print(freq_words_with_mismatch_and_reverse(text, k, d))
