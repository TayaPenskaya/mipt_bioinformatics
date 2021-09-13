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

def freq_words_with_mismatch(text, k, d):
    wmap = {}
    res = []
    for i in range(len(text)-k):
        pattern = text[i:i+k]
        ns = neighbors(pattern, d)
        for n in ns:
            if (n not in wmap):
                wmap[n] = 1
            else:
                wmap[n] += 1
    vmax = max(wmap.values())
    for k, v in wmap.items():
        if (v == vmax):
            res.append(k)

    return ' '.join(res)

with open('rosalind_ba1i.txt') as f:
    text = f.readline()[:-1]
    k, d = list(map(int, f.readline()[:-1].split()))

    with open('res.txt', 'w') as file:
         file.write(freq_words_with_mismatch(text, k, d))
