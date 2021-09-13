def hamming_distance(str1, str2):
    dist = 0
    for i in range(len(str1)):
        if (str1[i] != str2[i]):
            dist += 1
    return dist

def appr_matching(pattern, text, d):
    res = []

    for i in range(len(text)-len(pattern)+1):
        if (hamming_distance(text[i:i+len(pattern)], pattern) <= d):
            res.append(str(i))

    return ' '.join(res)

with open('rosalind_ba1h.txt') as f:
    pattern = f.readline()[:-1]
    text = f.readline()[:-1]
    d = int(f.readline()[:-1])

    with open('res.txt', 'w') as file:
        file.write(appr_matching(pattern, text, d))
