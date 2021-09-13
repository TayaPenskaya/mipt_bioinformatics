def get_clump_patterns(genome, k, L, t):
    kmap = {}
    for i in range(len(genome)-k+1):
        cur = genome[i:i+k]
        if cur not in kmap:
            kmap[cur] = [i]
        else:
            kmap[cur].append(i)

    res = []
    for key, ids in kmap.items():
        if (len(ids) >= t):
            fl = False
            for i in range(len(ids)-t+1):
                j = i+t-1
                if (ids[j]-ids[i] <= L-k):
                    fl = True

            if (fl):
                res.append(key)

    res.sort()
    return ' '.join(res)

with open('rosalind_ba1e.txt') as f:
    genome = f.readline()[:-1]
    k, L, t = list(map(int, f.readline()[:-1].split()))
    print(get_clump_patterns(genome, k, L, t))
