def skew_minimum(gstr):
    gmin = 0
    res = []
    cur = 0

    for i in range(len(gstr)):
        s = gstr[i]
        if (s == 'G'):
            cur += 1
        elif (s == 'C'):
            cur -= 1
        if (cur < gmin):
            gmin = cur
            res = [str(i+1)]
        elif (cur == gmin):
            res.append(str(i+1))

    return ' '.join(res)

with open('rosalind_ba1f.txt') as f:
    gstr = f.readline()[:-1]
    print(skew_minimum(gstr))
